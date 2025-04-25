# Ask the user to enter a word and store it in the variable 'letter'
letter = input("Enter any word of your choice: ")

# Create an empty string that will store the reversed word
string = ""

# Loop through each character in the original word
for let in letter:
    # Add the current character to the beginning of 'string' to build the reversed version
    string = let + string

    # Print the reversed string at the current stage of the loop
    print(f"Reverse of String: {string}")
