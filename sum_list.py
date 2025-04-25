# LIST OF NUMBERS

list_num = [10 ,20 ,30 ,40 ,50 ] # List containing 10 upto 50
sum =0 # Initialize the sum variable to 0

print("LIST OF NUMBERS")

for num in list_num: # Loop through each number in the list
    sum += num # Add the current number to the sum
    print(f"Current sum is {sum}") # Print the running sum at each step

print("\n") # Add spacing between examples

# CONCATENATING STRINGS IN A LIST

list_names = ["Adam", "Brian", "Shantel"] # List of strings
con_cat = "" # Initialize empty string

print("LIST OF NAMES")
for name in list_names: # Loop through each string in the list
    con_cat += name # Add current string to the concatenated result
    print(f"Current name is '{con_cat}") # Print the concatenated string

