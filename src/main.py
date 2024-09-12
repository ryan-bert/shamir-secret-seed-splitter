
def main():

    # Mode selection (CLI)
    mode = input("Select mode (split/reconstruct): ")
    # Mode validation
    if mode == "split":
        split_mode()                # Split mode
    elif mode == "reconstruct":
        reconstruct_mode()          # Reconstruct mode
    else:
        raise ValueError("Invalid mode. Please select 'split' or 'reconstruct'.")

def split_mode():

    # TODO: CLI for input type (private key/seed phrase) 

    # TODO: If seed phrase, covert to master private key
    # - CLI for seed phrase input
    # - Validate seed phrase
    # - Convert to master private key using BIP39/BIP32
    # - Convert key to hex

    # TODO: Validate private key 
    # - CLI for private key input 
    # - Convert key to hex (ie validate hex characters)

    # TODO: Split private key into shares using shamir.py

    # TODO: Reconstruct private key from shares using shamir.py to validate

    # TODO: Save shares to file(s) & print message to console

def reconstruct_mode():



if __name__ == "__main__":
    main()