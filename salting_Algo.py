import os
import hashlib

# Randomise the salt input value
my_salt = os.urandom(64)

# Add a subtext that will be encoded
my_text = 'passwordtext'.encode()

# Input the salt hash value
salt_hash = hashlib.pbkdf2_hmac('sha256', my_text, my_salt, 5000)

# Convert the hash into hex
hex_hash = salt_hash.hex()
print(hex_hash)

# Convet to byte_hash
byte_hash = salt_hash.fromhex(salt_hash.hex())
print(byte_hash)