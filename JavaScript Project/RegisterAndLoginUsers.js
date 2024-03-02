const bcrypt = require('bcrypt');

// Function for hashing password
function hashPassword(password) {
    // Hash a password for the first time, with a randomly-generated salt
    const hashedPassword = bcrypt.hashSync(password, 10);
    return hashedPassword;
}

// checking password
function checkPassword(password, hashedPassword) {
    // Checking hashed password against entered password
    return bcrypt.compareSync(password, hashedPassword);
}

// register user and password
function registerUser(username, password) {
    // hashing the password for storage
    const hashedPassword = hashPassword(password);
    // simulating storing the username and hashed password in a database
    userDatabase[username] = hashedPassword;
}

// user login
function loginUser(username, password) {
    // retrieve the hashed password from the database (simulated)
    const hashedPassword = userDatabase[username];
    if (hashedPassword) {
        // entered password against the stored hashed password
        if (checkPassword(password, hashedPassword)) {
            console.log("Login successful!");
        } else {
            console.log("Incorrect password.");
        }
    } else {
        console.log("User not found.");
    }
}

// user database (in-memory object)
const userDatabase = {};

// register a user
registerUser("HelloWorld!", "HelloWorld!123");

// attempt to login with correct password
loginUser("HelloWorld!", "HelloWorld!123");

// attempt to login with incorrect password
loginUser("HelloWorld!", "HelloWorld!000");
