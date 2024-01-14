import hashlib
import os
import binascii

def generate_salt():
    #generate a random salt
    return os.urandom(16)

def hash_password(password, salt):
    #combine the password and salt, then hash using SHA-256
    hashed_password = hashlib.sha256(salt + password.encode()).digest()
    
    #convert the binary digest to a hexadecimal representation
    hashed_password_hex = binascii.hexlify(hashed_password).decode('utf-8')
    
    return hashed_password_hex

def check_password(password, salt, hashed_password):
    #hashing the entered password with the stored salt
    entered_hash = hashlib.sha256(salt + password.encode()).digest()
    
    #converting the binary digest to a hexadecimal representation
    entered_hash_hex = binascii.hexlify(entered_hash).decode('utf-8')
    
    #comparing the calculated hash with the stored hash
    return entered_hash_hex == hashed_password


password_to_hash = "your_password"

#generate a salt
salt = generate_salt()

#hashing the password
hashed_password = hash_password(password_to_hash, salt)

print(f"Salt: {binascii.hexlify(salt).decode('utf-8')}")
print(f"Hashed Password: {hashed_password}")

#checking the password
entered_password = "your_password"
if check_password(entered_password, salt, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password.")
