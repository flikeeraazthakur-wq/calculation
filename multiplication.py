# multiplication.py

def multiply(a, b):
    return a * b


# Optional testing
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = multiply(num1, num2)
    print("Result:", result)