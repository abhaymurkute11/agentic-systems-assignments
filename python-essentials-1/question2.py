# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age_input = input("Enter your age: ")

# Check if age is numeric
if not age_input.isdigit():
    print("Invalid age input")
else:
    age = int(age_input)

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative")
    else:
        # Full name using string concatenation
        full_name = first_name + " " + last_name
        print("Full Name: " + full_name)
        print("You will be " + str(age + 1) + " next year")
