"""Yes/No checking function
based on 01_yes_no_v1
"""


# Functions go here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
         answer = "Yes"
         return answer

        #if they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")
07 lucky unicorn video 4:24sec ix this whole code

# Main routines go here
show_intructions = yes_no("have you played this game before? ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you Having fun? ")
print(f"You entered '{having_fun}'")