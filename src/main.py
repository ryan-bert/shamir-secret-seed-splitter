
def main():

    # TODO: Mode selection (CLI)
    mode = input("Select mode (split/reconstruct): ")

    if mode == "split":
        split_mode()
    elif mode == "reconstruct":
        reconstruct_mode()
    else:
        raise ValueError("Invalid mode. Please select 'split' or 'reconstruct'.")

def split_mode():


    # TODO: If seed phrase, covert to master private key
    # - Validate seed phrase
    # - Convert to master private key using BIP39/BIP32
    # - Convert key to hex

    # TODO: Validate private key 

    # TODO: Split private key into shares using shamir.py

    # TODO: Reconstruct private key from shares using shamir.py to validate

    # TODO: Save shares to file(s) & print message to console

def reconstruct_mode():



if __name__ == "__main__":
    main()