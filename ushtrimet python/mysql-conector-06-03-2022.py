import mysql.connector
#file do ta lidhim me mysql

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "QPALzm12."
)
print(mydb)
