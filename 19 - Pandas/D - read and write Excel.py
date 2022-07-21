
import pandas as pd

# create a dictionary of films
# films = {
#     "id": [1,2,3,5,6],
#     "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
#     "Released Date": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
#     "Run Time": [126, 121, 187,154, 194],
#     "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
# }

# # create a Pandas dataframe based upon this
# df = pd.DataFrame(films)

# # write the data to an Excel workbook
# df.to_excel("/Users/ikenna/Documents/GitHub/Python/19 - Pandas/films.xlsx",index=False,sheet_name="List of films")

# read in this file
new_df = pd.read_excel("/Users/ikenna/Documents/GitHub/Python/19 - Pandas/films.xlsx",sheet_name="List of films")

print(new_df)
