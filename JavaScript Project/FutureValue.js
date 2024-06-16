/*
Question: How can we calculate the future value of an annuity due with regular monthly contributions?

Formula:
The future value (FV) of an annuity due can be calculated using the formula:

FV = P × [(1 + r) × ((1 + r)^n - 1) / r]

- P is the monthly payment or contribution amount.
- r is the monthly interest rate.
- n is the total number of monthly contributions over the investment period.

Consider the following variables:
- P = 500 (Monthly payment)
- r = 0.06 / 12 (Monthly interest rate derived from 6% annual interest rate)
- n = 30 * 12 (Number of monthly contributions over 30 years)

*/



const annuityFutureValue = (annuityPayment, interestRate, numberOfPeriod) => {
    const future_value = annuityPayment * (((Math.pow(1 + interestRate, numberOfPeriod) - 1) / interestRate));
    console.log(`After ${numberOfPeriod / 12} years of contributing $${annuityPayment} at the end of each period with ${(interestRate * 12) * 100}% interest compounded monthly, the investor will have approximately $${future_value.toFixed(2)} in their retirement account.`);
}

let monthlyPayment = 500;
let annualInterestRate = 0.06; // 6%
let monthlyInterestRate = annualInterestRate / 12;
let numberOfMonths = 30 * 12;

annuityFutureValue(monthlyPayment, monthlyInterestRate, numberOfMonths);
