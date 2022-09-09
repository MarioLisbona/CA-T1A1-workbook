# creating the list of numbers
arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# printing the list of numbers
print("Original list\t", arr)

# Setting i to the value of 0 - the first element of the list
# iterating over the elments in the list while the i is less than the length of the list - 1 (zero index)
# and the current element is less than the next element.
i = 0
while ( i < len(arr) - 1) and (arr[i] < arr[i + 1]):
    # while true increment i
    i +=1
# I've left this in but all it does it print out the last index that is reached befre the while loop fails
print(i)

# Swap the current elemnt with the next elenent
arr[i], arr[i + 1] = arr[i + 1], arr[i]

# printing the new list with the first two elements that are out of order now put in order
print("New list\t", arr)


# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while (i < len(arr) - 1) and (arr[i] < arr[i+1]):
#     i +=1
# print(1)

# print(arr)
# arr[i], arr[i + 1] = arr[i + 1], arr[i]
# # arr[i] = arr[i+1]
# # arr[i+1] = arr[i]   
# print(arr)

