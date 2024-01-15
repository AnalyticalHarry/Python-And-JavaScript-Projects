#function to create celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    #formula to convert into fahrenheit
    converted_fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {converted_fahrenheit:.2f}°F")
    
#function to calculate into celsius
def fahrenheit_to_celsius(fahrenheit):
    #formula to convert into celsius
    converted_celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {converted_celsius:.2f}°C")

celsius_temperature = float(input("Temperature in Celsius: "))
celsius_to_fahrenheit(celsius_temperature)

fahrenheit_temperature = float(input("Temperature in Fahrenheit: "))
fahrenheit_to_celsius(fahrenheit_temperature)
