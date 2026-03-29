def multiply(a, b):
    return a * b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.\n")

def main():
    print("=" * 36)
    print("      Multiplication Calculator")
    print("=" * 36)

    while True:
        print("\nEnter two numbers to MULTIPLY (or 0 0 to exit):")
        num1 = get_number("Enter first number  : ")
        num2 = get_number("Enter second number : ")

        if num1 == 0 and num2 == 0:
            print("\nGoodbye! 👋")
            break

        result = multiply(num1, num2)
        display = int(result) if result == int(result) else result
        print(f"\n  ✅  {num1} * {num2} = {display}")

if __name__ == "__main__":
    main()