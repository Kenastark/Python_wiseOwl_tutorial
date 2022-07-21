
import pyodbc

cn = pyodbc.connect(
    "Driver=SQL Server;"
    "Server =.\sql2019;"
    "Database-Movies;"
    "Trusted_Connection=yes;"

)

# set up my SQL query
qry = "SELECT * FROM tblFilm ORDER BY Title"

# A cursor is what allows you to go row by row through the record

# create a cursor
csr = cn.cursor()

# execute a cursor
csr.execute(qry)

# fetch all rows
films = csr.fetchall()

# test if it works
print(films)

# clost database connection
cn.close()




