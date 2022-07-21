
from datetime import date, datetime



def get_age(ref_date:str) -> int:

    # create a variable to hold the date
    this_date = datetime.strptime(ref_date, "%d/%m/%Y")

    # get age in years
    return datetime.today().year -  this_date.year
    
# test it out
print(get_age("09/08/2010"))




