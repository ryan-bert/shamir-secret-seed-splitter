from src.encoding import seed_phrase_to_private_key
from src.shamir import secret_split, reconstruct

def main():

    # Input type selection (CLI)
    print("Split mode selected. Ensure input is located in ./split/input as 'private_key.txt' (hexadecimal) or 'seed_phrase.txt' (space-separated string).")
    input_type = input("\nSelect input type - private key (p)/seed phrase (s): ")
    
    # Input type validation
    if input_type == "private key" or input_type == "p":
        input_type = "private key"
    elif input_type == "seed phrase" or input_type == "s":
        input_type = "seed phrase"
    else:
        raise ValueError("Invalid input type. Please select 'private key' or 'seed phrase'.")
    
    # Read input from file & validate
    private_key = None
    if input_type == "private key":
        with open("./split/input/private_key.txt", "r") as file:
            hex_string = file.readline()
            try:
                byte_string = bytes.fromhex(hex_string)
                private_key = byte_string.hex()
            except ValueError as e:
                raise ValueError("Invalid private key format. Must be a valid hex string.") from e
    elif input_type == "seed phrase":
        with open("./split/input/seed_phrase.txt", "r") as file:
            seed_phrase = file.readline()
            private_key = seed_phrase_to_private_key(seed_phrase)

    # Split private key into shares
    shares = secret_split(int(private_key, 16), 3, 5)

    # Reconstruct private key from shares to validate
    reconstructed_private_key = reconstruct(shares)
    byte_string = bytes.fromhex(reconstructed_private_key[2:])
    reconstructed_private_key = byte_string.hex()
    if private_key != reconstructed_private_key:
        raise ValueError("Reconstructed private key does not match the original private key.")
    else:
        print("Shares successfully generated and validated.")

    # Save shares to file(s)
    for i, share in enumerate(shares):
        file_path = f'./split/output/share{i + 1}.txt'
        with open(file_path, 'w') as file:
            file.write(str(share))
    print("Shares saved to './split/output'.")

if __name__ == "__main__":
    main()