
import pandas as pd

# # create a dictionary of films
# films = {
#     "id": [1,2,3,5,6],
#     "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
#     "Released Date": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
#     "Run Time": [126, 121, 187,154, 194],
#     "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
# }

# # create a Pandas dataframe based upon this
# df = pd.DataFrame(films)

# # two ways to get subset of a dataframe
# # 1.Slicing - iloc
# # indexing - lock

# # slicing | rows are numbered from zero
# sub_frame = df.iloc[:3,1:]
# print(sub_frame)

# # alternate rows
# alt_rows = df.iloc[::2,::2]
# print(alt_rows)

# create a dictionary of films
films = {
    "id": [1,2,3,5,6],
    "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
    "Released Date": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
    "Run Time": [126, 121, 187,154, 194],
    "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
}

# create a Pandas dataframe based upon this
df = pd.DataFrame(films,index=[17,13,22,8,49])

# print out certain rows
certain_films = df.loc[[22,49,17]]
print(certain_films)

# it is faster to access rows by their index number






