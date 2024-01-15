function CurrencyConverter(Amount, FromCurrency, ToCurrency, ExchangeRate) {
    if (!ExchangeRate.hasOwnProperty(FromCurrency) || !ExchangeRate.hasOwnProperty(ToCurrency)) {
        console.log("Invalid currency code.");
        return null;
    }

    //replace the following line with your actual conversion logic
    const convertedAmount = Amount * ExchangeRate[ToCurrency] / ExchangeRate[FromCurrency];

    return convertedAmount;
}

function UserInput() {
    console.log("Welcome to the Currency Converter!");

    //assuming ExchangeRate is an object with currency codes as properties
    const ExchangeRate = {
        //replace these values with actual exchange rates
        'USD': 1.0, 
        'EUR': 0.85,         
        'GBP': 0.73,
        'JPY': 112.15,
        'AUD': 1.32,
        'CAD': 1.28,
        'INR': 74.94,
        'CNY': 6.38,
        'MXN': 20.04,
        //add more currencies as needed
    };

    //get data from the user
    const amount = parseFloat(prompt("Enter the amount: "));
    const fromCurrency = prompt("Enter the source currency code (e.g., USD): ").toUpperCase();
    const toCurrency = prompt("Enter the target currency code (e.g., EUR): ").toUpperCase();

    const result = CurrencyConverter(amount, fromCurrency, toCurrency, ExchangeRate);

    if (result !== null) {
        console.log(`${amount} ${fromCurrency} is equal to ${result} ${toCurrency}`);
    }
}

UserInput();
