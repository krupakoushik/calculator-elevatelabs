def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid input. Please enter a number 🙃")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the program...")
        break

    a = number("Enter A: ")
    b = number("Enter B: ")

    match choice:
        case '1':
            print(a, "+", b, "=", a + b)
        case '2':
            print(a, "-", b, "=", a - b)
        case '3':
            print(a, "*", b, "=", a * b)
        case '4':
            if b != 0:
                print(a, "/", b, "=", a / b)
            else:
                print("Division by zero is not possible 🙃")
        case _:
            print("P L E A S E  C H O O S E  A N  O P T I O N  F R O M  1  T O  5 :)")
