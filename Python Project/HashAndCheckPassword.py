#encryption library
import bcrypt

#function for hashing password
def hash_password(password):
    #hash a password for the first time, with a randomly-generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

#function to check password
def check_password(password, hashed_password):
    #checking hashed password against entered password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# 1. hashing a password
password_to_hash = "Hello World!"
hashed_password = hash_password(password_to_hash)
print(f"Original Password: {password_to_hash}")
print(f"Hashed Password: {hashed_password}")

# 2. checking a password
entered_password = "Hello World!"
if check_password(entered_password, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password.")