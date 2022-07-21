
# also known as "annonymous functions" - an alternative way to write a function,
#  provided that the function contains a single return (and no other statement)
# 
# Used when you have a function which only has a single return statement in.


# Look at 3 things:

# 1. Beasic lambda functions
# 2. Naming lambda functions
# 3. Multiple arguments

# NORMAL FUNCTIONS
# def cube(number:float) -> float:

#     return number ** 3

# # test this out
# print(cube(4))


# BASIC LAMBDA FUNCTIONS
# test_cube = (lambda x: x ** 3) (4)
# print(test_cube)


# NAMED LAMBDA FUNCTION 
# cube = lambda x: x ** 3
# print(cube(4))

# MULTIPLE ARGUMENTS
# lambda function to return a full name
full_name = lambda first_name, last_name: first_name + " " + last_name

# call this
print(full_name("kena", "Udeani"))



