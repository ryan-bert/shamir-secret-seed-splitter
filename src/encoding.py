import hmac
import hashlib
from mnemonic import Mnemonic

def seed_phrase_to_private_key(seed_phrase: str):
    # BIP39: Convert seed phrase (mnemonic) to seed
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(seed_phrase)
    
    # BIP32: Generate HMAC-SHA512 from seed.
    hmac_result = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    
    #  Master key is 1st 32 bytes
    master_key = hmac_result[:32]

    try:
        master_key = master_key.hex()
    except Exception as e:
        raise ValueError("Error converting master key to hex") from e
    
    return master_key