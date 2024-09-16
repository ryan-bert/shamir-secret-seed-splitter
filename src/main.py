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

import os

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
    elif input_type == "seed phrase":
        seed_phrase = input("Enter seed phrase: ")
        private_key = seed_phrase_to_private_key(seed_phrase)

    # Split private key into shares
    shares = secret_split(int(private_key, 16), 3, 5)

    # Reconstruct private key from shares to validate
    reconstructed_private_key = reconstruct(shares)
    byte_string = bytes.fromhex(reconstructed_private_key[2:])      # Remove"0x" prefix
    reconstructed_private_key = byte_string.hex()
    if private_key != reconstructed_private_key:
        raise ValueError("Reconstructed private key does not match the original private key.")

    # Get absolute path to 'output' directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, '../output')
    
    # Save shares to file(s)
    print("Shares generated successfully.")
    for i, share in enumerate(shares):
        file_path = os.path.join(output_dir, f"share{i+1}.txt")
        with open(file_path, "w") as file:
            file.write(str(share))

def reconstruct_mode():

    shares = []
    # Load shares from file(s)
    for i in range(5):
        file_path = f"../input/share{i+1}.txt"
        with open(file_path, "r") as file:
            share = file.read()
            shares.append(share)
    # Reconstruct private key from shares
    private_key = reconstruct(shares)
    # Print reconstructed private key to console
    print(f"Reconstructed private key: {private_key}")
    # Save reconstructed private key to file
    with open("../output/reconstructed_private_key.txt", "w") as file:
        file.write(private_key)

if __name__ == "__main__":
    main()