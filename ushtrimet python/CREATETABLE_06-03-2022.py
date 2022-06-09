import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)

#Krijimi i nje tabele brenda databazes: database="UshtrimiMsql"

kursori = mydb.cursor()
kursori.execute("CREATE TABLE Hobi (Hobi_id int primary key, Hobi_emri varchar(255), koment varchar (255))")


kursori.execute("CREATE TABLE Personi (Personi_id int primary key, Personi_emri varchar(255), Personi_mbiemri varchar (255), Mosha int, Pesha int, Datelinjda datetime)")