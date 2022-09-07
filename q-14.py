#A prime number is a whole number greater than 1 whose only factors are 1 and itself. A factor is a whole number that can be divided evenly into another number


#start loop, with variable *number* , from range of 1 and 101 (end of range is exclusive):
    #if *number* is greater than 1: (1 isnt a prime number)
        #start another loop with variable *x*, from range of 2 to *number*: 
        # (this loop will always finish 1 before *number* because we are using range)
        # (so if *number* is divisible, with no remainder, by any number before its self then it cant be a prime)
            #if *number* is divisible by *x* with no remainder:
                #not a prime number, break out of inner loop
        #else:
            #number was not divisible by any number between 2 and its self - 1, so its a prime.
            #Print Prime number


for number in range(1, 101):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(f'{number} is a prime number')
    