def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = P * R * T / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time):
    # Compound Interest formula: CI = P * (1 + (R / 100))^T - P
    compound_interest = principal * (1 + rate / 100)**time - principal
    return compound_interest

def main():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate: "))
        time = float(input("Enter the time period in years: "))

        simple_interest = calculate_simple_interest(principal, rate, time)
        compound_interest = calculate_compound_interest(principal, rate, time)

        print(f"\nSimple Interest: {simple_interest:.2f}")
        print(f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, rate, and time.")

#calling the main function directly
main()
