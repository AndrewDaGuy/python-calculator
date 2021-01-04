print("Select an operation!")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("------------")

while True:
    choice = input("Input > ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("First number > "))
        num2 = float(input("Second number > "))
        result = ""

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num1 == 0:
                print("Cannot divide by 0 :/")
                break

            if num2 == 0:
                print("Cannot divide by 0 :/")
                break

            result = num1 / num2
        print(" ")
        print("Result >>> ", result)
        break
    else:
        print("Invalid operation. :/")
