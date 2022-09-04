# # creating a bool for raining and setting user_input_rainig to 0 so the while loop will run at least once
# raining = False
# user_input_raining = 0

# #while loop to to force use to enter a digit for temperature
# #isdigit() will return false for anything but a number
# user_input_temp = input("\nWhat is the temperature outside? >> ")
# while not user_input_temp.isdigit():
#     print("Temp needs to be a number")
#     user_input_temp = input("\nWhat is the temperature outside? >> ")

# #while loop to forse user to enter y or n. User can enter Y or N as well, as the lower() function
# #is used to  convert user input to lowercase.
# #if elif statement changes the bool for raining to true of false and gives an error for any input besides
# #y or n
# while (user_input_raining != "y" and user_input_raining != "n"):
#     user_input_raining = input("Is it raining outside? y for yes, n for no >> ").lower()
#     if user_input_raining == "y":
#         raining = True
#     elif user_input_raining == "n":
#         raining = False
#     else:
#         print(f"\n{user_input_raining} is not a valid response")

# #if/elif/else statement to print out correct messages based on the the comparisona and logical operators
# #using round() and float() to convert the string inut to float then round to 1 decimal place.
# if raining and round(float(user_input_temp), 1) < 15:
#     print("\nIt's wet and cold")
# elif not raining and round(float(user_input_temp), 1) < 15:
#     print("\nIt's not raining but cold")
# elif not raining and round(float(user_input_temp), 1) >= 15:
#     print("\nIt's warm but not raining")
# else:
#     print("\nIt's warm and raining")


def rain_temp(raining, temperature):
    if raining and temperature < 15:
        print("\nIt's wet and cold")
    elif not raining and temperature < 15:
        print("\nIt's not raining but cold")
    elif not raining and temperature >= 15:
        print("\nIt's warm but not raining")
    else:
        print("\nIt's warm and raining")    


rain_temp(True, 14)
rain_temp(False, 14)
rain_temp(False, 15)
rain_temp(True, 46)


# if raining and temperature < 15:
#     print("\nIt's wet and cold")
# elif not raining and temperature < 15:
#     print("\nIt's not raining but cold")
# elif not raining and temperature >= 15:
#     print("\nIt's warm but not raining")
# else:
#     print("\nIt's warm and raining")
