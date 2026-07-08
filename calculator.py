print("== Welcome to Abdulrahman's Calculator ==")

while True:
    # Ask for the numbers and operation
    first_number = float(input("Enter your first number: "))
    operation = input("Enter operation (* / + -): ")
    second_number = float(input("Enter your second number: "))

    # Perform the calculation
    if operation == "*":
        print(first_number * second_number)

    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(first_number / second_number)

    elif operation == "+":
        print(first_number + second_number)

    elif operation == "-":
        print(first_number - second_number)

    else:
        print("Sorry, invalid operation!")

    # Ask if the user wants another calculation
    again = input("Do you want to use the calculator again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for using my calculator!")
        break