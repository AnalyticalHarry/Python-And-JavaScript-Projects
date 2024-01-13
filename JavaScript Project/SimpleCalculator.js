//This is a simple calculator implemented in JavaScript that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. 
//It prompts the user to select an operation and input two numbers. 
//The program ensures that the user enters a valid operation and valid numeric inputs (either integers or floats

// Addition of two numbers
function addition(num1, num2) {
    const sum = num1 + num2;
    console.log("Sum of two numbers is", sum);
}

// Subtraction of two numbers
function subtraction(num1, num2) {
    const sub = num1 - num2;
    console.log("Subtraction of two numbers is", sub);
}

// Division of two numbers
function division(num1, num2) {
    while (num2 === 0) {
        console.log("Cannot divide by zero");
        num2 = parseFloat(prompt("Enter a non-zero number for the second operand: "));
    }

    const div = num1 / num2;
    console.log("Division of two numbers is", div);
}

// Multiplication of two numbers
function multiplication(num1, num2) {
    const multi = num1 * num2;
    console.log("Multiplication of two numbers is", multi);
}

// Function to select operations
function calculation(user_input, num1, num2) {
    switch (user_input) {
        case "add":
            addition(num1, num2);
            break;
        case "sub":
            subtraction(num1, num2);
            break;
        case "div":
            division(num1, num2);
            break;
        case "multi":
            multiplication(num1, num2);
            break;
        default:
            console.log("Please enter a valid operation (add, sub, div, multi)");
    }
}

// UserInput function
function getUserInput() {
    let user_input;

    while (true) {
        user_input = prompt("Enter user operations: ");

        if (["add", "sub", "div", "multi"].includes(user_input)) {
            break;
        }

        console.log("Invalid operation. Please enter a valid operation (add, sub, div, multi).");
    }

    let num1;

    while (true) {
        num1 = parseFloat(prompt("Enter number one: "));

        if (!isNaN(num1)) {
            break;
        }

        console.log("Invalid input. Number one must be either a float or an integer. Please try again.");
    }

    let num2;

    while (true) {
        num2 = parseFloat(prompt("Enter number two: "));

        if (!isNaN(num2)) {
            break;
        }

        console.log("Invalid input. Number two must be either a float or an integer. Please try again.");
    }

    calculation(user_input, num1, num2);
}

getUserInput();
