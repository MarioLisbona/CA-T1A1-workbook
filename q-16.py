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

python = False
ruby = False
bash = False
git = False
html = False
tdd = False
css = False
javascript = False

candidate_total_skill_score = 0
candidate_skill_entered = False
full_skill_set = {"Python", "Ruby", "Bash", "Git", "HTML", "TDD", "CSS", "JavaScript"}
candidate_skill_set = set()



user_prompt()
press_to_continue()
user_prompt()

while not python or not ruby or not bash or not git or not html or not tdd or not css or not javascript:

    user_prompt()
    print("\n=================================================================================================")
    if candidate_skill_set:
        print(f"\tYour skillset: {candidate_skill_set}")
        print(f"\tYour skill score: {candidate_total_skill_score}")
    else:
        print("\tYour skillset: None")
        print(f"\tYour skill score: {candidate_total_skill_score}")
    print("=================================================================================================\n")

    candidate_skill_entered = input("\t**Python**  **Ruby**  **Bash**  **Git**  **HTML**  **TDD**  **CSS**  **JavaSCript**\n\tPlease enter a choice from the skills above >>")



    if candidate_skill_entered.lower() == "python":
        if not python:
            candidate_total_skill_score +=1
        python = True
        candidate_skill_set.add("Python")

    elif candidate_skill_entered.lower() == "ruby":
        if not ruby:
            candidate_total_skill_score +=2
        ruby = True
        candidate_skill_set.add("Ruby")

    elif candidate_skill_entered.lower() == "bash":
        if not bash:
            candidate_total_skill_score +=4
        bash = True
        candidate_skill_set.add("Bash")

    elif candidate_skill_entered.lower() == "git":
        if not git:
            candidate_total_skill_score +=8
        git = True
        candidate_skill_set.add("Git")

    elif candidate_skill_entered.lower() == "html":
        if not html:
            candidate_total_skill_score +=16
        html = True
        candidate_skill_set.add("HTML")

    elif candidate_skill_entered.lower() == "tdd":
        if not tdd:
            candidate_total_skill_score +=32
        tdd = True
        candidate_skill_set.add("TDD")

    elif candidate_skill_entered.lower() == "css":
        if not css:
            candidate_total_skill_score +=64
        css = True
        candidate_skill_set.add("CSS")

    elif candidate_skill_entered.lower() == "javascript":
        if not javascript:
            candidate_total_skill_score +=128
        javascript = True
        candidate_skill_set.add("JavaScript")

    elif candidate_skill_entered.lower() == "c":
        break
    else:
        print("\n====================================================================================================")
        print(f"\t{candidate_skill_entered} is not a valid selection!\n\tPlease try again")
        print("======================================================================================================\n")
        press_to_continue()
        


os.system('cls||clear')
print("====================================================================================================\n")
print("\tThankyou for applying for the junior developer role.\n")
print(f"\tYour skill set is: {candidate_skill_set}")
print(f"\tYour score is: {candidate_total_skill_score}")

if not full_skill_set.difference(candidate_skill_set):
    print("\n\tYou are skilled in every option!\n\tYou're the prefect candidate!")
else:
    print("\n\tBelow is a list of skills we think you could work on:")
    print(f"\t{full_skill_set.difference(candidate_skill_set)}")
print("======================================================================================================")