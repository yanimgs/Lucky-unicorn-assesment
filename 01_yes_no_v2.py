""" LU Yes / No
Simplifies the input by converting it to lower case. Also, accepts y or abbreviations.
Prints result of user choice as well as input - for testing
"""

# Ask the user if they have played before
show_instructions = input("Have you played this game before? :").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

#if they say no, output 'Display Instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}'")