# NESTING RANGES

# test for prime numbers
highest = 100

# outer loop
for test_number in range(2,highest+1):

    # test for 2
    if test_number == 2:
        print(test_number)
        continue

    # set flag if prime
    if_prime = True

    for possible_prime in range(2,test_number):

        # try to divide test number by this possible prrime
        if test_number % possible_prime  == 0:

            # this wasn't prime!
            if_prime = False
            break
    
    # if it's prime print out
    if if_prime:
        print(test_number)

print("That's it") 



# prime number is divisible only by itself and 1
# algorithm is a set of steps