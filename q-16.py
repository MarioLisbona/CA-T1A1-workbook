# Imprt OS library for press_to_continue function and clear screen function
import os

# User prompt fuction with information on how to use the program
def user_prompt():
    """
    This function clears the screen each time and prints a user prompt with instructions on how to use the program
    """    
    os.system('cls||clear')
    print("|===============================================================================================|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\tWelcome to the application for the junior developer role at ACME Corporation.\t\t|")
    print("|\tIn order for us to asses your skill level, please select any of the skills\t\t|")
    print("|\tfrom the list below that you have experience with.\t\t\t\t\t|")
    print("|\tOnce you have finished, hit the 'c' key and we will display your eligibilty score.\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t**Python**  **Ruby**  **Bash**  **Git**  **HTML**  **TDD**  **CSS**  **JavaScript**\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|===============================================================================================|")

# prompt user to press any key to contine - program execution is fronzen until a key press happens
def press_to_continue():
    """
    This function freezes the program execution and prints a press any key to continue message.
    Once a key is pressed it exits
    """   
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n\tPress any key to continue...\"'\n")
    os.system('cls||clear')
    print()


def format_string(k):
    """
    This function will return a formatted string.
    It capitalises all keys except for: uppercase for html, tdd and css, Uppercase s and j for javascript

    Args:
        k (string): Key for the current iteration of dictionary

    Returns:
        string: Formatted string
    """    
    if k == "html" or k == "tdd" or k == "css":
        return k.upper()
    elif k == "javascript":
        #create a dict with letters to swap
        swaps = {"j": "J", "s": "S"}
        #iterate over the string "javascript" for every j or s found gets returns the capitalised letter.
        #join appends the return values to an empty string
        return "".join(swaps.get(i, i) for i in "javascript")
    else:
        return k.capitalize()

# variable for candidate's total skill score
candidate_total_skill_score = 0

#dictionary with skill set and associated values
full_skill_set = {
    "python": 1,
    "ruby": 2,
    "bash": 4,
    "git": 8,
    "html": 16,
    "tdd": 32,
    "css": 64,
    "javascript": 128
}

#dictionary to hold appplicants skill set
candidate_skill_set = {}

#calling userprompt for first time with no skillset listes - just insctructions
user_prompt()

#wait for keypress,
press_to_continue()

#There are 8 skills. While loop will be true for 7th skill entered, when the 8th skill(last one) is entered this loop will run, return to the condition and it will fail so the while loop will exit at the end of the 8th iteration
while len(candidate_skill_set) <= 7:
    # display user prompt each time - this creates the effect of the user prompt never leaving, when in fact the screen is being cleared at the beginning of every user_prompt function call
    user_prompt()

    #if the dictionary candidate_skill_set has items, print only the keys
    #else print "none"
    print("\n=================================================================================================")
    if candidate_skill_set:
        print("\tYour skillset:")
        #iterate over candidate_skill_set dictionary 
        #Pass key as argument to format_string function to format each key accordingly
        for key in candidate_skill_set:
            print("\t\t\t\u27A4", format_string(key))
    else:
        print("\tYour skillset: None")
    print("=================================================================================================\n")

    #prompting user to enter a skill. lower() at the end to converts user input to lowercase
    candidate_skill_entered = input("\t**Python**  **Ruby**  **Bash**  **Git**  **HTML**  **TDD**  **CSS**  **JavaSCript**\n\tPlease enter a choice from the skills above (C to (C)omplete application) >>  ").lower()

    #using get() - scan candidate_skill_set for the user input. get() will return none (false) if the user input has already been entered (is already a key in the dictionary)
    #if the skill entered is not a key in the candidate_skill_set dict
    #then iterate over the full_skill_set dictionary and return the key and value on each iteration using items() method
    #if the current key equals the user input create a new key value pair with the current key and value with line 104: candidate_skill_set[key] = value
    #line 105 will take the current value and increment candidate_total_skill_score by that value
    if not candidate_skill_set.get(candidate_skill_entered):
        for key, value in full_skill_set.items():
            if key == candidate_skill_entered:
                candidate_skill_set[key] = value
                candidate_total_skill_score += value

    #else print an error message - The skill has already been entered
    else:
        print("\n====================================================================================================")
        print(f"\t{format_string(candidate_skill_entered)} has alredy been entered!\n\tPlease try again")
        print("======================================================================================================\n")
        press_to_continue()

    #If the user input is C or c (Completed) then escape out of the while loop with break statement
    if candidate_skill_entered == "c":
        break

    #if the user input is not a listed skill, print an error message
    if not candidate_skill_entered in full_skill_set:
        print("\n====================================================================================================")
        print(f"\t{candidate_skill_entered} is not a valid selection!\n\tPlease try again")
        print("======================================================================================================\n")
        press_to_continue()


#The user has entered C or c (Completed) so we escape out of the while loop.
#clear the screen and print the candidates results
os.system('cls||clear')
print("====================================================================================================\n")
print("\tThankyou for applying for the junior developer role.\n")

#iterate over the keys in candidate_skill_set and print each one to the screen

#iterate over candidate_skill_set dictionary 
#Pass key as argument to format_string function to format each key accordingly
for key in candidate_skill_set:
    print("\tSkill Recorded  \u2713", format_string(key))

#printing the total score for the candidate
print(f"\n\tYour skill score is \u27A4 {candidate_total_skill_score}")

#If the candidate has entered every skill, they have a perfect score. They get the job!
#When all 8 skills are not entered show message with skills not entered and value that could improve score.
if len(candidate_skill_set) == 8:
    print("\n\tCongratulations! You got the job, you're the perfect candidate!")
else:
    print("\n\tBelow is a list of skills that will improve your score:\n")
for key, value in full_skill_set.items():
    if not key in candidate_skill_set:
        if key == "python":
            print("\t\u27A4", value, "point:\t\u272D Experience with", format_string(key))
        else:
            print("\t\u27A4", value, "points:\t\u272D Experience with", format_string(key))
print("\n======================================================================================================")