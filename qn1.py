import random

# Function for sum of array
def sumArray(n):

    # initialize the sum
    sum = 0
    # from the first counting number to the total number given
    # the sum is equal to the previous sum plus the next number
    for i in range(1, n + 1, 1):
        sum = sum + i

    print(sum)


#Testing
sumArray(10)
sumArray(10)
sumArray(10000)
sumArray(1000000)
sumArray(1000000000)
