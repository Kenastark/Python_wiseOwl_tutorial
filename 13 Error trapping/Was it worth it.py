
# create a function to calculate the reciprocal of a number
def reciprocal(number:float) -> float:

    # check if a number
    if type(number) == float or type(number) == int:
        test_number = float(number)
    else:
        print("Not a number")
        return None

    # divide by zero
    if test_number == 0:
        print("Divide by zero")
        return None


    # return the reciprocal
    return (1/test_number)


# test it out
answer = reciprocal("bob")
if answer == None:
    pass
else:
    print(answer)






