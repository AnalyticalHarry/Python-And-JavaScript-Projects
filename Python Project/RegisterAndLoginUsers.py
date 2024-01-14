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

#function to register user and password
def register_user(username, password):
    #hashing the password for storage
    hashed_password = hash_password(password)
    #simulating storing the username and hashed password in a database
    user_database[username] = hashed_password

#function for login user name and password
def login_user(username, password):
    #retrieve the hashed password from the database (simulated)
    hashed_password = user_database.get(username)
    if hashed_password:
        #check the entered password against the stored hashed password
        if check_password(password, hashed_password):
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

#simulated user database (in-memory dictionary)
user_database = {}

#register a user
register_user("HelloWorld!", "HelloWorld!123")

#attempt to login with correct password
login_user("HelloWorld!", "HelloWorld!123")

#attempt to login with incorrect password
login_user("HelloWorld!", "HelloWorld!000")