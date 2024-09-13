import hmac
import hashlib
from mnemonic import Mnemonic

def seed_phrase_to_private_key(seed_phrase: str):
    # BIP39: Convert seed phrase (mnemonic) to seed
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(seed_phrase)
    
    # BIP32: Generate HMAC-SHA512 from seed.
    hmac_result = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    
    # The master key is the first 32 bytes (256 bits) of the HMAC-SHA512 result
    master_key = hmac_result[:32]
    
    return master_key