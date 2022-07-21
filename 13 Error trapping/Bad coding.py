
#  create a function to calculate the reciprocal of a number
def reciprocal(number:float) -> float:
    
    return (1/number)

#  trap for an error
try:

    # do something dodgy
    print(reciprocal("bob"))

except ZeroDivisionError:

    # take remedial action
    print("CAN'T DIVIDE BY ZERO")

except TypeError:
    print("Make sure you use a number")

except:
    print("Something else went wrong")



