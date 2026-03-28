try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum: {a + b}")
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(f"Division: {a / b}")
except ValueError:
    print("Invalid input")