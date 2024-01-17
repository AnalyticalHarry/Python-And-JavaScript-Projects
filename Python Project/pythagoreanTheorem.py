import math

#function hypotenuse 
def hypotenuse(perpendicular, base):
    c = math.sqrt(perpendicular**2 + base**2)
    return c

#function perpendicular 
def perpendicular(hypotenuse, base):
    a = math.sqrt(hypotenuse**2 - base**2)
    return a

#function base
def base(hypotenuse, perpendicular):
    b = math.sqrt(hypotenuse**2 - perpendicular**2)
    return b

#user input for calculating hypotenuse/perpendicular/base
calculation_type = input("What do you want to calculate? (hypotenuse/perpendicular/base): ").lower()
if calculation_type == "hypotenuse":
    perpendicular = float(input("Enter the length of the perpendicular (a): "))
    base = float(input("Enter the length of the base (b): "))
    result = hypotenuse(perpendicular, base)
    print(f"The length of the hypotenuse (c) is: {result}")
elif calculation_type == "perpendicular":
    hypotenuse = float(input("Enter the length of the hypotenuse (c): "))
    base = float(input("Enter the length of the base (b): "))
    if hypotenuse >= base: 
        result = perpendicular(hypotenuse, base)
        print(f"The length of the perpendicular (a) is: {result}")
    else:
        print("Invalid input. Hypotenuse must be greater than or equal to the base.")
elif calculation_type == "base":
    hypotenuse = float(input("Enter the length of the hypotenuse (c): "))
    perpendicular = float(input("Enter the length of the perpendicular (a): "))
    if hypotenuse >= perpendicular: 
        result = base(hypotenuse, perpendicular)
        print(f"The length of the base (b) is: {result}")
    else:
        print("Invalid input. Hypotenuse must be greater than or equal to the perpendicular.")
else:
    print("Invalid input. Please specify 'hypotenuse', 'perpendicular', or 'base' for calculation.")
