# print(candidate_skill_entered.capitalize())
# swaps = {"j": "J", "s": "S"}
# print(("".join(swaps.get(i, i) for i in "javascript") == "JavaScript"))

# Imprt OS library for press_to_continue function and clear screen function
import os

# User prompt fuction with information on how to use the program
def user_prompt():
    os.system('cls||clear')
    print("|===============================================================================================|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\tWelcome to the application for the junior developer role at ACME Corporation.\t\t|")
    print("|\tIn order for us to asses your skill level, please select any of the skills\t\t|")
    print("|\tfrom the list below that you have experience with.\t\t\t\t\t|")
    print("|\tOnce you have finished, hit the 'c' key and we will display your eligibilty score.\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t**Python**  **Ruby**  **Bash**  **Git**  **HTML**  **TDD**  **CSS**  **JavaScript**\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|===============================================================================================|")

# prompt user to press any key to contine - program frozen till key press
def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n\t\tPress any key to continue...\"'\n")
    os.system('cls||clear')
    print()

# variable for candidate's total skill score
candidate_total_skill_score = 0

#variable to prevent empty dict being displayed for skill set
candidate_skill_entered = False

#dict with skill set and associated value
full_skill_set = {
    "python": 1, 
    "ruby": 2, 
    "bash": 4, 
    "git": 8, 
    "html": 16, 
    "tdd": 32, 
    "css": 64, 
    "javascript": 128}

#dic tto hold appplicants skill set
candidate_skill_set = {}

user_prompt()
press_to_continue()
user_prompt()

# If the skill entered by the user is has not already been entered, find the skill/value in the full_skill dict and add it to user skill set dict
while len(candidate_skill_set) <= 7:
    user_prompt()
    print("\n=================================================================================================")
    if candidate_skill_set:
        print(f"\tYour skillset: {candidate_skill_set}")
    else:
        print("\tYour skillset: None")

    print("=================================================================================================\n")
    candidate_skill_entered = input("\t**Python**  **Ruby**  **Bash**  **Git**  **HTML**  **TDD**  **CSS**  **JavaSCript**\n\tPlease enter a choice from the skills above >>").lower()

    if not candidate_skill_set.get(candidate_skill_entered):
        for key, value in full_skill_set.items():
            if key == candidate_skill_entered:
                candidate_skill_set[key] = value
                candidate_total_skill_score += value
    
    if candidate_skill_entered.lower() == "c":
        break
   
   
os.system('cls||clear')
print("====================================================================================================\n")
print("\tThankyou for applying for the junior developer role.\n")

for key in candidate_skill_set:
    if key == "html" or key == "tdd" or key == "css":
        print("\tSkill Recorded  \u2713", key.upper())
    elif key == "javascript":
        swaps = {"j": "J", "s": "S"}
        print("\tSkill Recorded  \u2713", "".join(swaps.get(i, i) for i in "javascript"))
    else:
        print("\tSkill Recorded  \u2713", key.capitalize())
    
print(f"\n\tYour skill score is: {candidate_total_skill_score}")


if len(candidate_skill_set) == 8:
    print("\n\tCongratulations! You got the job, you're the perfect candidate!\n")
print("\n======================================================================================================")



# print(f"\tYour skill set is: {candidate_skill_set}")
# print(f"\tYour score is: {candidate_total_skill_score}")



