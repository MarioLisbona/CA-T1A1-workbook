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

temp = 0

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

