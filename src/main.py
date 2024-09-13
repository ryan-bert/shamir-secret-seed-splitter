from shamir import secret_split, reconstruct
from encoding import seed_phrase_to_private_key

def main():

    # Mode selection (CLI)
    mode = input("Select mode - split (s)/reconstruct (r): ")
    # Mode validation
    if mode == "split" or mode == "s":
        split_mode()                                # Split mode
    elif mode == "reconstruct" or mode == "r":
        reconstruct_mode()                          # Reconstruct mode
    else:
        raise ValueError("Invalid mode. Please select 'split' or 'reconstruct'.")

def split_mode():


    # Input type selection (CLI)
    input_type = input("Select input type - private key (p)/seed phrase (s): ")
    # Input type validation
    if input_type == "private key" or input_type == "p":
        input_type = "private key"
    elif input_type == "seed phrase" or input_type == "s":
        input_type = "seed phrase"
    else:
        raise ValueError("Invalid input type. Please select 'private key' or 'seed phrase'.")
    

    # Private key validation & hex conversion 
    private_key = None
    if input_type == "private key":
        hex_string = input("Enter private key (hex): ")
        try:
            byte_string = bytes.fromhex(hex_string)
            private_key = byte_string.hex()
        except ValueError as e:
            raise ValueError("Invalid private key format. Must be a valid hex string.") from e
    # Seed phrase validation & conversion
    elif input_type == "seed phrase":
        seed_phrase = input("Enter seed phrase: ")
        private_key = seed_phrase_to_private_key(seed_phrase)

    # Split private key into shares
    shares = secret_split(private_key, 3, 5)

    # Reconstruct private key from shares using shamir.py to validate
    reconstructed_privat_key = reconstruct(shares)
    byte_string = bytes.fromhex(reconstructed_privat_key)
    reconstructed_privat_key = byte_string.hex()
    if private_key == reconstructed_privat_key:
        print("Private key successfully reconstructed from shares.")
    else:
        raise ValueError("Reconstructed private key does not match original private key.")

    # TODO: Save shares to file(s) & print message to console


def reconstruct_mode():
    pass


if __name__ == "__main__":
    main()