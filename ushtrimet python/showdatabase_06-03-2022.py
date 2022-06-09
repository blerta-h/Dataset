import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="QPALzm12."
	)

#kriju nje kursor qe lidhet direkt me atributin e lidhjes me databze
kursori = mydb.cursor()


kursori.execute("SHOW DATABASES")

#krijojm ne python nje for loop per gjetjen e databazes me kete emer dhe printimi
for x in kursori:
    print(x)