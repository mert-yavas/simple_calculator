from art import logo 
from replit import clear

def main():
    print(logo)  
    n1 = float(input("What's the firs number?: "))  
    print("+\n-\n*\n/")  # Display the available operations.

    while True:  # Start a loop to allow continuous calculations.
        operator = input("Pick an operation: ")  
        n2 = float(input("What's the next number?: "))  
        n3 = calc(n1, operator, n2)  # Perform the calculation based on the chosen operator.
        print(f"{n1} {operator} {n2} = {n3}")  

        while True:  # Inner loop to ask the user if they want to continue with the result.
            ask_again = input(f"Type 'y' to continue calculating with {n3}, or type 'n' to start a new calculation: ")
            if ask_again == "y":
                n1 = n3  # Set the new first number as the result of the previous calculation.
                calc(n1, operator, n2)  # Continue with a new operation.
                break
            elif ask_again == "n":
                clear()  # Clear the console and start a new calculation.
                main()  # Restart the main function.
            else:
                print("Please enter 'y' or 'n' letter")  # Prompt for valid input.
        continue  # Continue with the outer loop.

def calc(n1 ,operator , n2):
    # Calculation function that performs basic arithmetic operations.
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "*":
        return n1 * n2
    if operator == "/":
        return n1/n2

if __name__ == "__main__":
    main()  # Run the main function when the script is executed.
