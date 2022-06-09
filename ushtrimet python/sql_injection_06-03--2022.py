import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)

kursori = mydb.cursor()
#Te gjinden te gjithe emrat e hobit qe ne kolonen koment permban tekstin "Kapjen e peshqeve.""
sql_query = "SELECT * FROM Hobi WHERE koment = %s"
kom = ("Kapjen e peshqeve.",)

kursori.execute(sql_query, kom)

rezultati = kursori.fetchall()

for x in rezultati:
    print(x)