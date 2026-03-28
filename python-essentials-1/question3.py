# Get user input
name = input("Enter your name: ")
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
        # Greet the user
        print("Hello " + name)

        # Age category
        if age < 13:
            print("You are a Child")
        elif age >= 13 and age <= 17:
            print("You are a Teenager")
        elif age >= 18 and age <= 59:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")

        # Voting eligibility
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")