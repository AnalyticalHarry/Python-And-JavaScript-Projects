// formula for hypotenuse
function calculateHypotenuse(perpendicular, base) {
    return Math.sqrt(perpendicular ** 2 + base ** 2);
}

// formula for  perpendicular
function calculatePerpendicular(hypotenuse, base) {
    return Math.sqrt(hypotenuse ** 2 - base ** 2);
}

// formula for  base
function calculateBase(hypotenuse, perpendicular) {
    return Math.sqrt(hypotenuse ** 2 - perpendicular ** 2);
}

// function to perform calculation
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

// calculating hypotenuse
performCalculation("hypotenuse", 3, 4); 

//Author : Hemant Thapa
//Date code pushed in Git : 27.02.2024
