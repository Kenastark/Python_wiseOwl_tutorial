
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

print(df)
print("\n")
# # single column statistics
# average_run_time =  df["Run Time"].mean()
# print(average_run_time)

# # more than one column statistics
# mult_col_stats = df[["Title", "Genre"]].nunique()
# print("\n")
# print(mult_col_stats)
# print(type(mult_col_stats))

# to display different statistics for different columns
# stats = df.agg({
#     "Genre": ["count","nunique"],
#     "Run Time": ["min", "max", "nunique"]
# })

# print(stats)

# print("\n")

# average runtime by genre
# average_runtime_by_genre = df[["Genre","Run Time"]].groupby("Genre").mean() # it takes the mean of anything that it is not grouping by, that is by "Run Time"

# print(average_runtime_by_genre)

# different statistics grouped by genre
# agg function builds up a dictionary of statistics to be displayed
final_stats = df[["Genre", "Run Time"]].groupby("Genre").agg({
    "Run Time": ["min","max", "mean"]
})

print(final_stats)


