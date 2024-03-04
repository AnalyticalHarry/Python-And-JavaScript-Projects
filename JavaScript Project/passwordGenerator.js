// function for generating password
function passwordGenerator(length = 10, uppercase = true, lowercase = true, numbers = true, symbols = true) {
    let characters = '';
    const uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowercaseLetters = 'abcdefghijklmnopqrstuvwxyz';
    const digits = '0123456789';
    const symbolChars = '!@#$%^&*()_+{}:"<>?[];,./`~';

    // include uppercase, lowercase, numbers, and symbols in passwords
    if (uppercase) characters += uppercaseLetters;
    if (lowercase) characters += lowercaseLetters;
    if (numbers) characters += digits;
    if (symbols) characters += symbolChars;

    // at least one character type is selected
    if (!characters.length) {
        console.log('Please choose at least one character type');
        return '';
    }

    // generate the password by randomly selecting characters from the combined set
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    return password;
}

const password = passwordGenerator(12, true, true, true, true);
console.log(`Generated Password: ${password}`);
