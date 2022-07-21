

# create a function to calculate the reciprocal of a number
def reciprocal(number:float) -> float:
    try:
        return (1/number)
    except:
        print("Can not create reciprocal")
        return None

# test it oit
answer = reciprocal(2)

if answer == None:
    pass
else:
    print(answer)

