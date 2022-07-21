
import pandas as pd

# create a dictionary of films
films = {
    "Id": [1,2,3,5,6],
    "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
    "Released Date": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
    "Run Time": [126, 121, 187,154, 194],
    "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
}

# create a Pandas dataframe based upon this
df = pd.DataFrame(films)

# general information about a dataframe
# print(df.info())

# information on datatype
# print(df.dtypes)

# summary statistics
# print(df.describe())

# top and bottom rows
# print(df.tail(3))

# show specific columns
print(df[["Title","Id"]]) # you need to parse in what you are using, if a list you need the extra [] to denote its a list



