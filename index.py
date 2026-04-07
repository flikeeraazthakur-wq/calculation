# add.py

def add(a, b):
    """
    Function to return the sum of two numbers
    """
    return a + b


def run_addition():
    """
    Function to take user input and display result
    """
    print("Addition Operation")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    result = add(num1, num2)
    print("Result:", result)


# Run this file independently
if __name__ == "__main__":
    run_addition()
