import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12."
	)

#kriju nje kursor qe lidhet direkt me atributin e lidhjes me databze
kursori = mydb.cursor()

#MSQL - Krijimi i nje databse ne MYSQL OSE SQL SERVER
#CREATE DATABASE
kursori.execute("CREATE DATABASE ushtrimimsql1")