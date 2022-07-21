
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

# fetch 5 rows
# films = csr.fetchmany(5)

# # loop over rows listing them out
# for film in films:

#     print("{0} was made in {1}".format(film.Title,film.Released))

while True:

    film_row = csr.fetchone()

    # did this return anything?
    if not film_row:
        break

    # stop at Pirates film
    film_title = film_row.Title

    print(film_title)

    if "pirates" in str(film_title).lower():
        break

cn.close()