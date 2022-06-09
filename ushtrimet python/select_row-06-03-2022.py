import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Fremont4#",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="UshtrimiMsql"
	)


kursori = mydb.cursor()

#Le te fshihet rreshti (record) kur emri i hobit eshte "Mbledhjen e Pullave"
sql_query = "DELETE FROM Hobi WHERE Hobi_emri = 'Mbledhjen e Pullave'"

kursori.execute(sql_query)

import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12.",
	#kur ne jemi qas mysql dhe kemi ne databzen e krijuar "UshtrimiMsql"
	database="ushtrimimsql1"
	)


kursori = mydb.cursor()

#Le te fshihet rreshti (record) kur emri i hobit eshte "Mbledhjen e Pullave"
sql_query = "DELETE FROM Hobi WHERE Hobi_emri = 'Mbledhjen e Pullave'"

kursori.execute(sql_query)

#nese deshironi qe te reflektoj ndryshimi ose modifikimi i juaj ne databaze perdoret 

mydb.commit()
#nese ndryshimi sipas sql_query eshte i suksesshem atehere le te printohet mesazhi i tille:
print("numri i rreshtave te fshire sipas kushtit eshte: ", kursori.rowcount)