import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)

kursori = mydb.cursor()

#Ti rendisni ne baze alfabetike emrat e Hobit
#ASC (A-Z)
#DESC (Z-A)
#sql_query = "SELECT Hobi_emri FROM Hobi ORDER BY Hobi_emri"
sql_query = "SELECT Hobi_emri FROM Hobi ORDER BY Hobi_emri DESC"

kursori.execute(sql_query)

rezultati = kursori.fetchall()

for x in rezultati:
	print(x)