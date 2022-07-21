
for num in range(2,11):

    # show different powers of 2 to 10
    print(

        "Square of " + str(num).rjust(2) + " is " +
        str(num ** 2).ljust(5) + " cube is " +
        str(num ** 3).rjust(5) + " and 4th power is " +
        str(num ** 4).center(10)
    )