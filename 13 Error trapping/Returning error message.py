
# create a function to calculate the reciprocal of a number
def reciprocal(number:float, errmsgs:list) -> float:
    
    try:
        return (1/number)
    except:
        errmsgs.append("Something went wrong")
        return None

error_messages = []

answer = reciprocal(0,error_messages)

# test whether an error occured
if len(error_messages) == 0:
    print(answer)
else:
    print(error_messages[0])



