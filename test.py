# import sys

# cheese_list = ['Parmigiano', 'Pecorino', 'Bocconcini', 'Treccia']
# for cheese in cheese_list:
#     print(cheese)

# example_tuple = ('Mario', 'Lisbona', 42, 1979, 'Male')
# example_list = ['Mario', 'Lisbona', 42, 1979, 'Male']

# print(sys.getsizeof(example_tuple))
# print(sys.getsizeof(example_list))



# def function_with_no_return():
#     pass

# function_with_no_return()
# print(function_with_no_return())

# def add_person(name, people=[]):
#     people.append(name)

#     return people

# #works if we  pass an exisiting list to the function

# # people = ['Mario', 'Ali', 'John', 'Denise']

# # add_person('Alana', people)

# # print(people)

# x = add_person('Jon')
# print(x)

# y = add_person('Snow')

# print(y)

# temp = 0

# if temp < 15:
#     print("It's cold outside")
#     print("It would be a good idea to wear a jacket")
# elif temp > 15 and temp < 20:
#     print("It's warm outside")
#     print("It would be a good idea to wear jeans and a t-shirt")
# elif temp > 20 and temp < 30:
#     print("It's really warm outside")
#     print("It would be a good idea to wear shorts, t-shirt and a hat")
# else:
#     print("It's really hot, go to the beach")


def rain_temp(raining, temperature):
    """
    This functions prints out a different message depending on whether its raining or not and what the temperature is.

    Args:
        raining (Bool): true of false pool - whether its raining or not.
        temperature (int): The temperature in degrees.
    """    
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
rain_temp(False, 46)



if temp < 15:
    print("It's cold outside")
    print("It would be a good idea to wear a jacket")
elif temp > 15 and temp < 20:
    print("It's warm outside")
    print("It would be a good idea to wear jeans and a t-shirt")
elif temp > 20 and temp < 30:
    print("It's really warm outside")
    print("It would be a good idea to wear shorts, t-shirt and a hat")
else:
    print("It's really hot, go to the beach")
