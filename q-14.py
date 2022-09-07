#A prime number is a whole number greater than 1 whose only factors are 1 and itself. A factor is a whole number that can be divided evenly into another number



for number in range (1, 101):
    #prime numbers start at 2
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)  