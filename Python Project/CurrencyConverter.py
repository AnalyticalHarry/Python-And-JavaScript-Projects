#exchange rates
exchange_rates = {'USD': 1.0, 'EUR': 0.85, 
                  'GBP': 0.73,'JPY': 112.15,
                  'AUD': 1.32,'CAD': 1.28,
                  'INR': 74.94,'CNY': 6.38,
                  'MXN': 20.04,}

#function for converting currency
def currency_converter(amount, from_currency, to_currency, exchange_rates):
    #print function, if currency didn't exist inside dictonary
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency code.")
        return None
    #formula to convert currency 
    converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    #return converted amount
    return converted_amount

#function for user input
def userInput():
    print("Welcome to the Currency Converter!")
    #get data from user 
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    #performing conversion rate
    result = currency_converter(amount, from_currency, to_currency, exchange_rates)
    # Display the result
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}.")
        
#calling function userInput
userInput()