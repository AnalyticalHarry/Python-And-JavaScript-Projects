// import math module
const Math = require('math');

// class definition for Triangle
class Triangle {
    // Constructor to initialize the sides of the triangle
    constructor(side1, side2, side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    // method to check if the triangle is valid
    is_valid() {
        return (this.side1 + this.side2 > this.side3) && 
               (this.side2 + this.side3 > this.side1) && 
               (this.side3 + this.side1 > this.side2);
    }

    // method to determine the type of triangle (Equilateral, Isosceles, or Scalene)
    type() {
        if (!this.is_valid()) {
            return "Invalid triangle";
        }
        if (this.side1 === this.side2 && this.side2 === this.side3) {
            return "Equilateral triangle";
        } else if (this.side1 === this.side2 || this.side2 === this.side3 || this.side3 === this.side1) {
            return "Isosceles triangle";
        } else {
            return "Scalene triangle";
        }
    }

    // method to determine the type of angles in the triangle (Acute, Right, or Obtuse)
    angle_type() {
        if (!this.is_valid()) {
            return "Invalid triangle";
        }
        // sorting sides
        let sides = [this.side1, this.side2, this.side3];
        sides.sort((a, b) => a - b);
        // determining the sides of the triangle
        let [a, b, c] = sides;

        if (a**2 + b**2 > c**2) {
            return "Acute triangle";
        } else if (a**2 + b**2 === c**2) {
            return "Right triangle";
        } else {
            return "Obtuse triangle";
        }
    }

    // method to calculate the area of the triangle
    area() {
        if (!this.is_valid()) {
            return "Invalid triangle";
        }
        // using Heron's formula
        let s = (this.side1 + this.side2 + this.side3) / 2;
        let area = Math.sqrt(s * (s - this.side1) * (s - this.side2) * (s - this.side3));
        return area.toFixed(2);
    }

    // Method to print the output
    toString() {
        return `Triangle with sides ${this.side1.toFixed(2)}, ${this.side2.toFixed(2)}, ${this.side3.toFixed(2)}`;
    }
}

// equilateral triangle with Acute angles
const equilateral_acute = new Triangle(5, 5, 5);
console.log("Equilateral triangle with Acute angles:");
console.log(equilateral_acute.toString());
console.log("Type:", equilateral_acute.type());
console.log("Angle Type:", equilateral_acute.angle_type());
console.log("Area:", equilateral_acute.area(), "\n");

// isosceles triangle with Right angles
const isosceles_right = new Triangle(4, 4, Math.sqrt(32));
console.log("Isosceles triangle with Right angles:");
console.log(isosceles_right.toString());
console.log("Type:", isosceles_right.type());
console.log("Angle Type:", isosceles_right.angle_type());
console.log("Area:", isosceles_right.area(), "\n");

// scalene triangle with Obtuse angles
const scalene_obtuse = new Triangle(7, 9, Math.sqrt(155));
console.log("Scalene triangle with Obtuse angles:");
console.log(scalene_obtuse.toString());
console.log("Type:", scalene_obtuse.type());
console.log("Angle Type:", scalene_obtuse.angle_type());
console.log("Area:", scalene_obtuse.area(), "\n");
