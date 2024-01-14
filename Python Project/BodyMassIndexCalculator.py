# Body mass index function
def body_mass_index(weight: float, height: float, age: int, sex: str):
    try:
        body_mass_index = weight / (height * height)
        if age < 18:
            return "BMI categories for children and adolescents are age- and sex-specific."
        elif age >= 18:
            if body_mass_index < 18.5:
                return "Underweight"
            elif 18.5 <= body_mass_index < 25.0:
                return "Normal weight"
            elif 25.0 <= body_mass_index < 30.0:
                return "Overweight"
            elif 30.0 <= body_mass_index < 35.0:
                return "Obese (Class 1)"
            elif 35.0 <= body_mass_index < 40.0:
                return "Obese (Class 2)"
            else:
                return "Invalid age input"
        else:
            return "Invalid age input"
    except ZeroDivisionError:
        return "Error: Height cannot be zero"

#main function for input parameters
def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        age = int(input("Enter your age: "))
        sex = input("Enter your sex (male/female): ").lower()
    except ValueError:
        print("Invalid input. Please enter numeric values for weight, height, and age.")
        return

    bmi_category = body_mass_index(weight, height, age, sex)
    print(f"\nYour BMI category is: {bmi_category}")

main()