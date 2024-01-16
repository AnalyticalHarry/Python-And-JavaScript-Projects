// creating function for body mass index
function bodyMassIndex(weight, height, age, sex) {
    try {
        //formula for body mass index
        const bodyMassIndex = weight / (height * height);
        if (age < 18) {
            return "BMI categories for children and adolescents are age- and sex-specific.";
            //if user ager is greater or equal to eighteen 
        } else if (age >= 18) {
            if (bodyMassIndex < 18.5) {
                return "Underweight";
            } else if (18.5 <= bodyMassIndex && bodyMassIndex < 25.0) {
                return "Normal weight";
            } else if (25.0 <= bodyMassIndex && bodyMassIndex < 30.0) {
                return "Overweight";
            } else if (30.0 <= bodyMassIndex && bodyMassIndex < 35.0) {
                return "Obese (Class 1)";
            } else if (35.0 <= bodyMassIndex && bodyMassIndex < 40.0) {
                return "Obese (Class 2)";
            } else {
                return "Invalid age input";
            }
        } else {
            return "Invalid age input";
        }
    } catch (error) {
        return "Error: Height cannot be zero";
    }
}
//function for user input
function main() {
    try {
        const weight = parseFloat(prompt("Enter your weight in kilograms: "));
        const height = parseFloat(prompt("Enter your height in meters: "));
        const age = parseInt(prompt("Enter your age: "));
        const sex = prompt("Enter your sex (male/female): ").toLowerCase();
        const bmiCategory = bodyMassIndex(weight, height, age, sex);
        console.log(`\nYour BMI category is: ${bmiCategory}`);
    } catch (error) {
        console.error("Invalid input. Please enter numeric values for weight, height, and age.");
    }
}

main();
