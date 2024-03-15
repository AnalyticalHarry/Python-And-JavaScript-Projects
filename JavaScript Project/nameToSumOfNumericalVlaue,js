function getNumericalValue(name) {
    // convert the name to uppercase to handle both uppercase and lowercase letters
    name = name.toUpperCase();
    
    let numericalValue = 0;

    // iterate through each character in the name
    for (let i = 0; i < name.length; i++) {
        let charCode = name.charCodeAt(i);
        
        // check if the character is a letter
        if (charCode >= 65 && charCode <= 90) { // ASCII codes for A-Z
            // Subtract 64 to map A to 1, B to 2, and so on
            numericalValue += charCode - 64;
        }
    }

    return numericalValue;
}

console.log(getNumericalValue("Harry")); // H: 8 , A: 1, R: 18, R: 18 & Y: 25
// 8 + 1 + 18 + 18 + 25
