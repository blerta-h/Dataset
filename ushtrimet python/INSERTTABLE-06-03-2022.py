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

#Insertimi apo mbushja e kolonave me rreshta ose parametra(vlera)
sql = "INSERT INTO Hobi (Hobi_id, Hobi_emri, koment) VALUES ( %s,%s, %s) " 
val = ( 1,"Pikturim", "Aplikimi bojës, pigment, ngjyra o")