def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Welcome to the Python Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        cont = input("Do you want to perform another calculation? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
