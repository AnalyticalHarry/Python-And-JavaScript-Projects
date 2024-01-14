import random, string

#function for generating password
def password_generator(length=10, uppercase=True, lowercase=True, numbers=True, symbols=True):
    #empty string to store the characters based on user's choices
    characters = ""
    #include uppercase, lowercase, numbers and symbols in passwords
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
     #at least one character type is selected
    if not any([uppercase, lowercase, numbers, symbols]):
        print("please choose at least one character type")
        return
    #generate the password by randomly selecting characters from the combined set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = password_generator(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True)
print(f"Generated Password: {password}")