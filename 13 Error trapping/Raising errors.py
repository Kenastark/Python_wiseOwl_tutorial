
# create a function to calculate the reciprocal of a number
def reciprocal(number:float) -> float:
    
    try:
        return (1/number)
    except:
        raise Exception("Problem occured", "Probably a divide by zero error")

# test it out
try:
    print(reciprocal(2))
except Exception as problems:
    
    
    # list out problems
    for p in problems.args:
        print(p)





