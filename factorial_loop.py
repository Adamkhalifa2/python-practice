# Prompt user to enter a number
number = int(input("Enter any number: "))

# Initialize factorial variable
factorial = 1

# Check if the number is 0
if number == 0:
    print(f"The factorial of {number} is {factorial}")
else:
    # Multiply all numbers from 1 to the entered number
    for num in range(1, number + 1):
        factorial *= num

    # Print the result after the loop
    print(f"The factorial of {number} is {factorial}")
