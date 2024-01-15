//function for celsius to fahrenheit
function CelsiusToFahrenheit(celsius){
    converted_fahrenheit = (celsius * 9/5) + 32
    console.log(`'${celsius}'°C is equal to '${converted_fahrenheit}'°F`)
}

// function for fahrenheit to celsius
function FahrenheitToCelsius(fahrenheit){
    converted_celsius = (fahrenheit - 32) * 5/9
    console.log(`'${fahrenheit}'°C is equal to '${converted_celsius}'°F`)
}


//user input
CelsiusTemperature = parseFloat(prompt("Temperature in Celsius: "))
CelsiusToFahrenheit(CelsiusTemperature)

FahrenheitTemperature = parseFloat(prompt("Temperature in Fahrenheit: "))
FahrenheitToCelsius(FahrenheitTemperature)
