# Ask the user to enter a number and convert it to an integer
n = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
s = 0

# Create a copy of the number so the original number 'n' is not changed
num = n

# Loop to extract each digit and add it to the sum
while num > 0:
    # Get the last digit using modulo
    s += num % 10

    # Remove the last digit from the number using floor division
    num = num // 10

# Print the final sum of digits
print("Sum of digits is:", s)
