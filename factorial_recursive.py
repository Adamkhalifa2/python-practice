# Define a function called 'factorial' that takes one parameter 'n'
def factorial(n):
    # Base case: if n is 0, return 1 (since 0! = 1)
    if n == 0:
        return 1

    # Recursive case: multiply n by the factorial of (n - 1)
    return n * factorial(n - 1)

# Ask the user to input a number and convert it to an integer
number = int(input("Enter any number: "))

# Call the factorial function and store the result
result = factorial(number)

# Print the final result
print(f"Factorial of {number} is {result}")
