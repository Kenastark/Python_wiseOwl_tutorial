
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

# sort by genre, and then by title
sorted_df = df.sort_values(by=["Genre","Title"],ascending=True)
print(sorted_df)

# # filter this to show all films lasting more than 130 minutes
# filtered_df = sorted_df[sorted_df["Run Time"] > 130]
# print(filtered_df)
print("\n")
# filter to show all films lasting 121 or 194 minutes
filtered_df2 = sorted_df[sorted_df["Run Time"].isin([121,194])]
print(filtered_df2)
