 # PROMPT WHERE THE USER ENTERS HIS / HER NUMBER
my_number = int(input("Enter you're number please:"))


if my_number % 2 == 0: # Checks if the number is divisible by two
    print(f"Your number {my_number} is even".format(my_number)) # If it is even , print a message saying so
else:
    print(f"Your number {my_number} is odd ".format(my_number)) # If it is even , print a message saying so