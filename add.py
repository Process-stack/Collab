# simple_calculator.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Divide")

    choice = input("Enter choice (1/2): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()