
from datetime import date, datetime

# FUNTION 1: Get the age in relation to today's date
def get_age(ref_date:str) -> int:

    """
        Returns the age of something
    """


    # create a variable to hold the date
    this_date = datetime.strptime(ref_date, "%d/%m/%Y")

    # get age in years
    return datetime.today().year -  this_date.year

# FUNCTION 2: Get the lines from a file
def film_lines(file_path: str, file_name:str) -> list:

    """
        Arguments:
        =========
        File path       where to find the path
        File name       what the file is called
    """

    # open the file
    with open(file_path + file_name) as films_file:

        # get all the lines
        lines = films_file.read().splitlines()[1:]
    return lines

# FUNTION 3: get the duration of a movie
def get_duration(minutes: int) -> str:
    
    """
        Takes in a runtime in minutes and spits out a text description
    """

    if not isinstance(minutes,int):
        return "NO SUCH NUMBER"

    # get the number of minutes
    mins = minutes % 60

    # get the number of hours
    hours = int((minutes - mins) / 60)
 
    # the hours as text
    hours_text = " hours" if hours >= 2 else "hour"

    # the minute aas text
    if mins == 0:
        minute_text = ""
    elif mins ==1:
        minute_text = " and 1 minute"
    else:
        minute_text = " and {0} minute".format(mins)

    # return the final string of text
    return str(hours) + hours_text + minute_text
