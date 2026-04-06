# day2_calculator.py

print("=== Simple Calculator ===")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("+  -  *  /")

        op = input("Enter operator: ")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operator")

        again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")
