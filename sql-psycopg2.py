import psycopg2


# Connect to chinook database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51] )

# Query 6 - Select all from "Album" list where "ArtistId" is #44
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Test"])

# fetch the results (mulitple)
results = cursor.fetchall()


# fetch the result (sinlge)
# results = cursor.fetchone()

# close the connection
connection.close()


# print results
for result in results:
    print(result)


