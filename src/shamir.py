from sympy import nextprime
import random
from sympy import mod_inverse

def secret_split(secret, threshold, num_shares):
    """
    Splits a secret into multiple shares using Shamir's Secret Sharing Scheme (SSSS).
    
    Parameters:
    - secret (int): The secret to be split (non-negative integer less than 2^256).
    - threshold (int): The minimum number of shares required to reconstruct the secret.
    - num_shares (int): The total number of shares to generate.
    
    Returns:
    - List[Tuple[int, int]]: A list of (x, y) pairs representing the shares.
    
    Raises:
    - ValueError: If the threshold is less than 2, num_shares is less than threshold, 
                  or if the secret is outside the valid range.
    """

    # Validate input
    if threshold < 2:
        raise ValueError("Threshold must be at least 2")
    if num_shares < threshold:
        raise ValueError("Number of shares must be greater than or equal to the threshold")
    if secret < 0 or secret >= 2**256:
        raise ValueError("Secret must be a non-negative integer less than 2^256")

    # Set prime number (p) for finite field
    p = nextprime(2**256)

    # Generate random coefficients for polynomial
    coefficients = [random.randint(1, p-1) for _ in range(threshold-1)]
    # Set constant term to secret
    coefficients.insert(0, secret)

    # Generate shares
    shares = []
    for i in range(num_shares):
        x = i + 1
        # Evaluate polynomial (Horner's method for efficiency)
        y = sum([coefficients[j] * pow(x, j, p) for j in range(threshold)]) % p
        shares.append((x, y))

    return shares


def reconstruct(shares):
    """
    Reconstructs the secret from a list of shares using Lagrange interpolation.
    
    Parameters:
    - shares (List[Tuple[int, int]]): A list of (x, y) pairs, where at least `threshold`
                                      shares must be provided for successful reconstruction.
    
    Returns:
    - str: The reconstructed secret as a hexadecimal string.
    """
    
    # Set prime number (p) for finite field
    p = nextprime(2**256)
    secret = 0
    
    # Lagrange interpolation
    for i, (x_i, y_i) in enumerate(shares):
        # Compute the Lagrange basis polynomial for x_i
        numerator = 1
        denominator = 1
        for j, (x_j, _) in enumerate(shares):
            if i != j:
                numerator = (numerator * (-x_j)) % p
                denominator = (denominator * (x_i - x_j)) % p
        
        # Compute the modular inverse of denominator mod p
        lagrange_coefficient = (numerator * mod_inverse(denominator, p)) % p
        # Add the contribution of current term to secret
        secret = (secret + y_i * lagrange_coefficient) % p
    
    return hex(secret)