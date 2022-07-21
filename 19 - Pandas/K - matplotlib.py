
import pandas as pd
import matplotlib.pyplot as plt

# create a dictionary of films
films = {
    "Id": [1,2,3,5,6],
    "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
    "Released Date": ["1993-06-11","2002-05-03","2005-12-14","2006-07-14","1998-01-23"],
    "Run Time": [126, 121, 187,154, 194],
    "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
}

# create a Pandas dataframe based upon this
df = pd.DataFrame(
    films,
    index= ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"]# index makes it quicker to access data
)

# plot the runtime minutes against the film name
plt.plot(df["Run Time"])

plt.show()