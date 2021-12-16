
# Super digits
def superDigit(n, k):
    # based on the input, p is calculated by duplicating
    # the number n, k times
    p = n * k

    # it is a repetitive process that goes on till the sum is a single digit
    # the while loop keeps the function running till the sum is a single digit
    while len(p) > 1:
        # initiate the total sum to zero
        sum_of_digits = 0
        # add the individual digit to each other
        for digit in p:
            sum_of_digits += int(digit)
        # run the sum again to make sure it is a single digit
        # the sum becomes p again
        p = str(sum_of_digits)

    return p


# Testing
print("Test 1: ", superDigit('985556666', 2))

print("Test 2: ", superDigit('78353682892183', 12))