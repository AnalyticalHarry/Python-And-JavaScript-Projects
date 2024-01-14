function calculateSimpleInterest(principal, rate, time) {
    // Simple Interest formula: SI = P * R * T / 100
    const simpleInterest = (principal * rate * time) / 100;
    return simpleInterest;
}

function calculateCompoundInterest(principal, rate, time) {
    // Compound Interest formula: CI = P * (1 + (R / 100))^T - P
    const compoundInterest = principal * (Math.pow((1 + rate / 100), time)) - principal;
    return compoundInterest;
}

function main() {
    try {
        const principal = parseFloat(prompt("Enter the principal amount: "));
        const rate = parseFloat(prompt("Enter the annual interest rate: "));
        const time = parseFloat(prompt("Enter the time period in years: "));

        const simpleInterest = calculateSimpleInterest(principal, rate, time);
        const compoundInterest = calculateCompoundInterest(principal, rate, time);

        console.log(`\nSimple Interest: ${simpleInterest.toFixed(2)}`);
        console.log(`Compound Interest: ${compoundInterest.toFixed(2)}`);
    } catch (error) {
        console.error("Invalid input. Please enter numeric values for principal, rate, and time.");
    }
}

main();
