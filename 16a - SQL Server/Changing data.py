
import pyodbc
def run_query(sql:str, *,if_action:bool) -> list:

    # create a connection to SQL Server database
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

    # run the required query
    csr.execute(sql)

    # either return the rows of data
    # or commit the action to change data
    if if_action:

        csr.commit()
        return None

    else:
        table = csr.fetchall()

         # close this connection
        cn.close() 

        return table

# reduce the Bee Movie Oscars
run_query("UPDATE tblFilm SET Oscars=1 WHERE Title='Bee Movie'", if_action=True)


# list out the films
films = run_query("SELECT * FROM tblFilm ORDER BY Title", if_action=False)
for film in films:
    print(film.Title, int(film.Oscars))
   