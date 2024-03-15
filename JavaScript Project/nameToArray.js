function getNumericalValue(name) {
    // mapping of letters to numbers
    const letterMapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    };

    let numericalValues = [];

    // convert the name to uppercase to handle both uppercase and lowercase letters
    name = name.toUpperCase();

    // iterate through each character in the name
    for (let i = 0; i < name.length; i++) {
        let char = name[i];
        if (letterMapping[char]) {
            numericalValues.push(letterMapping[char]);
        }
    }

    return numericalValues;
}

console.log(getNumericalValue("Harry")); //[ 8  1  18  18  25]
