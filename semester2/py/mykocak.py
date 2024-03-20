'''database connection for mykocak.db'''
import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursos = sqliteConnection.cursor()
    print("Database and Successfully Connected to SQLite")

    sqlite_select_query = """SELECT * from SqliteDb_developers"""
    cursos.execute(sqlite_select_query)
    records = cursos.fetchall()
    print("SqLite Database Version is : ", records)
    cursos.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
