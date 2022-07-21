
import pyodbc

    # create a connection to SQL Server database
cn = pyodbc.connect(
    "Driver=SQL Server;"
    "Server =.\sql2019;"
    "Database-Movies;"
    "Trusted_Connection=yes;"

)

# create a cursor
csr = cn.cursor()

# create SQL statement
sql_command = 'EXEC ListFilms ?, ?'
values = (' t', 0)

# run the stored procedure
csr.execute(sql_command,values)

# action query
# csr.commit()

films = csr.fetchall

print(films)

# close connection
cn.close()









