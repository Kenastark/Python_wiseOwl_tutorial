
import pandas as pd

# create a dictionary of films
films = {
    "id": [1,2,3,5,6],
    "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
    "Released Date": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
    "Run Time": [126, 121, 187,154, 194],
    "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
}

# create a Pandas dataframe based upon this
df = pd.DataFrame(films)
# print(type(df))
# print(df)

# create a list
film_titles = ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"]

# create a Pandas series based on this
film_series = pd.Series(film_titles)
print(type(film_series))
print(film_series)


