import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)

kursori = mydb.cursor()

kursori.execute("SELECT * FROM Hobi")
#i paraqet krejt rreshtate insertuara ne tabele
rezultati = kursori.fetchall()

#nese deshirojme ta paraqesin nje rresht te insertuar ne tabele
kursori.execute("SELECT * FROM Hobi")
rezultati = kursori.fetchone()

print(rezultati)

for x in rezultati:
	print(x)