import sys

cheese_list = ['Parmigiano', 'Pecorino', 'Bocconcini', 'Treccia']
for cheese in cheese_list:
    print(cheese)

example_tuple = ('Mario', 'Lisbona', 42, 1979, 'Male')
example_list = ['Mario', 'Lisbona', 42, 1979, 'Male']

print(sys.getsizeof(example_tuple))
print(sys.getsizeof(example_list))