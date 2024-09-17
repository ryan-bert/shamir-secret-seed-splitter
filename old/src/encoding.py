import hmac 
import hashlib
from mnemonic import Mnemonic

def seed_phrase_to_private_key(seed_phrase: str, passphrase: str = '') -> str:
    # Create Mnemonic instance
    mnemo = Mnemonic("english")
    
    # Validate the seed phrase
    if not mnemo.check(seed_phrase):
        raise ValueError("Invalid seed phrase: contains words not in the BIP39 word list or has the wrong format.")
    
    # Convert the valid seed phrase (mnemonic) to seed using BIP39
    seed = mnemo.to_seed(seed_phrase, passphrase)
    
    # BIP32: Generate HMAC-SHA512 from seed.
    hmac_result = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    
    # Master key is the first 32 bytes (256 bits)
    master_key = hmac_result[:32]
    
    # Convert the master key to hex
    return master_key.hex()