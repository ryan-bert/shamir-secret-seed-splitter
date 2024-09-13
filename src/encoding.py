import hmac
import hashlib
from mnemonic import Mnemonic

def seed_phrase_to_private_key(seed_phrase: str, passphrase: str = '') -> str:
    # BIP39: Convert seed phrase (mnemonic) to seed
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(seed_phrase, passphrase)
    
    # BIP32: Generate HMAC-SHA512 from seed.
    hmac_result = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    
    # Master key is the first 32 bytes (256 bits)
    master_key = hmac_result[:32]
    
    # Convert the master key to hex
    return master_key.hex()