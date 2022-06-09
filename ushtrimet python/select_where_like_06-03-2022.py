import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)

kursori = mydb.cursor()

kursori = mydb.cursor()

sql_query = "SELECT * FROM Hobi WHERE Hobi_emri LIKE 'P%'"

kursori.execute(sql_query)

rezultati = kursori.fetchall()

for x in rezultati:
	print(x)
