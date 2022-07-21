# WHILE LOOPS

counter = 0

while True:

    counter += 1

    # test if gone too far
    if counter >= 100:
        break
    
    # if divisible by 3
    if counter % 3 != 0:
        continue

    print(counter, "Fizz")

print("That's it")

# 'break' exits the loop automatically. You drop out and executes the
# next statement following it

# 'continue' does not exit the loop but goes on to the next iteration of it
# It will ignore any subsequent statements and go back up to the while
# condition at the top of the loop and start with the next iteration around it.