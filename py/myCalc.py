def calculator():
    print("This is my simple calculator")

    print("Select an operation:")

    print("1. Add")

    print("2. Subtract")

    print("3. Multiply")

    print("4. Divide")

    operation = input("Enter the number corresponding to your operation: ")

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    if operation == "1":

        result = num1 + num2

        print(f"The result of {num1} + {num2} is {result}")

    elif operation == "2":

        result = num1 - num2

        print(f"The result of {num1} - {num2} is {result}")

    elif operation == "3":

        result = num1 * num2

        print(f"The result of {num1} * {num2} is {result}")

    elif operation == "4":

        if num2 == 0:

            print("Error! Division by zero.")

        else:

            result = num1 / num2

            print(f"The result of {num1} / {num2} is {result}")

    else:
        
        print("Invalid operation. Please choose a valid option.")

# Call the calculator function
calculator()
