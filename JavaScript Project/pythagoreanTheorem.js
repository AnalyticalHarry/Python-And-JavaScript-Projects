// Function to calculate hypotenuse
function calculateHypotenuse(perpendicular, base) {
    return Math.sqrt(perpendicular ** 2 + base ** 2);
}

// Function to calculate perpendicular
function calculatePerpendicular(hypotenuse, base) {
    return Math.sqrt(hypotenuse ** 2 - base ** 2);
}

// Function to calculate base
function calculateBase(hypotenuse, perpendicular) {
    return Math.sqrt(hypotenuse ** 2 - perpendicular ** 2);
}

// Example usage
// Assuming you want to calculate one of the sides or hypotenuse
// and the inputs are provided through some other means (e.g., web form)

function performCalculation(calculationType, side1, side2) {
    let result;
    switch (calculationType.toLowerCase()) {
        case "hypotenuse":
            result = calculateHypotenuse(side1, side2);
            console.log(`The length of the hypotenuse (c) is: ${result}`);
            break;
        case "perpendicular":
            if (side1 >= side2) {
                result = calculatePerpendicular(side1, side2);
                console.log(`The length of the perpendicular (a) is: ${result}`);
            } else {
                console.log("Invalid input. Hypotenuse must be greater than or equal to the base.");
            }
            break;
        case "base":
            if (side1 >= side2) {
                result = calculateBase(side1, side2);
                console.log(`The length of the base (b) is: ${result}`);
            } else {
                console.log("Invalid input. Hypotenuse must be greater than or equal to the perpendicular.");
            }
            break;
        default:
            console.log("Invalid input. Please specify 'hypotenuse', 'perpendicular', or 'base' for calculation.");
    }
}

// Example call to performCalculation
performCalculation("hypotenuse", 3, 4); // For calculating hypotenuse
