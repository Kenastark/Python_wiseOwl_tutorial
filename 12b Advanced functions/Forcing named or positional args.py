
# See more about pros and cons of BMI as a measurement of health at https://www.bbc.co.uk/news/health-43895508

# you can force positional or named arguments:

# - anything before the /, if used, must be positional
#  - anything after the *, if used, must be keyword
#               def f(pos1, pos2, / pos_or_kwd, *, kwd1, kwd2):

# pos1 and pos2 must be positional arguments
# kwd1 and kwd2 must be keyword arguments

def bmi(height:float,*, weight:float) -> float:
    body_mass_index  = weight/ (height ** 2)
    return body_mass_index

# churchill's BMI
churchill_bmi = bmi(height=1.68,weight=95)
print(churchill_bmi)

# Stalin's BMI 
# stanlin_bmi = bmi(1.65, 65)
# print(stanlin_bmi)





