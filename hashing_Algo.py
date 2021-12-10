import hashlib

# My password
my_password = 123

# Hashing function that converts the password into hash
def password_hash(my_password):
    hash_function = hashlib.sha256() # Using hash 256
    hash_function.update(b"the password")
    hash_results = hash_function.hexdigest()
    print(hash_results) # Printing the results

password_hash(my_password)