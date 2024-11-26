def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b. Validates division by zero."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def get_operation_choice():
    """Prompts the user to choose an operation."""
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                print("Invalid choice. Please choose a valid operation.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def get_numbers():
    """Prompts the user to input two numbers."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def calculator():
    """Main calculator loop."""
    print("Welcome to the Python Calculator!")
    while True:
        choice = get_operation_choice()
        if choice == 5:
            print("Thank you for using the calculator. Goodbye!")
            break
        
        num1, num2 = get_numbers()

        if choice == 1:
            print(f"The result is: {add(num1, num2)}")
        elif choice == 2:
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"The result is: {result}")
        
        print("\n--- Operation Complete ---\n")

if __name__ == "__main__":
    calculator()
