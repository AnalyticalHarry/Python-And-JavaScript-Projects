function passwordGenerator(length = 10, uppercase = true, lowercase = true, numbers = true, symbols = true) {
    //empty string to store the characters based on user's choices
    let characters = "";

    //include uppercase, lowercase, numbers, and symbols in passwords
    if (uppercase) {
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }
    if (lowercase) {
        characters += "abcdefghijklmnopqrstuvwxyz";
    }
    if (numbers) {
        characters += "0123456789";
    }
    if (symbols) {
        characters += "!@#$%^&*()-_+=<>?/{}[]|";
    }

    //at least one character type is selected
    if (!uppercase && !lowercase && !numbers && !symbols) {
        console.log("Please choose at least one character type");
        return;
    }

    //generate the password by randomly selecting characters from the combined set
    let password = "";
    for (let i = 0; i < length; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length));
    }

    return password;
}

const generatedPassword = passwordGenerator(12, true, true, true, true);
console.log(generatedPassword);
