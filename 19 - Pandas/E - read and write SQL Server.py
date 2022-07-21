
import pandas as pd
import pyodbc 

# # create a dictionary of films
# films = {
#     "id": [1,2,3,5,6],
#     "Title": ["Jurassic Park", "Spider-man", "King-Kong", "Superman Returns","Titanic"],
#     "ReleasedDate": ["1993-06-11","1993-06-11","1993-06-11","1993-06-11","1993-06-11"],
#     "RunTime": [126, 121, 187,154, 194],
#     "Genre": ["Adventure", "Action", "Adventure", "Action", "Romance"]
# }

# # create a Pandas dataframe based upon this
# df = pd.DataFrame(films)

# # create a connection to the database
# cn = pyodbc(
#     "Driver=SQL Server;"
#     "Server=.\sql2019;"
#     "Database=Movies;"
#     "Trusted_Connection=yes;"
# )
# # a cursor is something which allows you to display records from a database or execute commands against it

# # create a cursor
# csr = cn.cursor()

# # loop over rows of the dataframe
# for index_number, row in df.iterrows():

#     # insert this row into database table
#     csr.execute(
#         "INSERT INTO tblFilm (Id, TItle, ReleaseDate, RunTime, Genre) VALUES (?,?,?,?,?)",
#         row.Id,row.Title,row.ReleeaseDate,row.RunTime,row.Genre
#     )

# # commit these changes
# cn.commite()

# # close down connection
# cn.close()



# READ INFO FROM THE DATABASE

# create a connection to the database
cn = pyodbc(
    "Driver=SQL Server;"
    "Server=.\sql2019;"
    "Database=Movies;"
    "Trusted_Connection=yes;"
)

# create a query
sql_query = "SELECT * FROM tblFilm ORDER BY Title"

# read in the data
film_dataframe = pd.read_sql(sql_queryl,cn)

# close down the connnection
cn.close()

# check it works
print(film_dataframe)