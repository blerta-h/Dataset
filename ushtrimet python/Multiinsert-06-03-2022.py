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
val = [(2,"Peshkim","Kapjen e peshqeve."),
	   (3,"Zhytje nën ujë","Futja nën ujë me ose pa aparatin e frymëmarrjes (zhytje/frymë-mbajtja)."),
	   (4,"Shah","Dy lojtarët kanë 16 shifra secili. Ata lëvizin ato nga tetë-me-tetë rrjet sipas rregullave të veçanta."),
	   (5,"Letërsi"," Leximi i librave."),
	   (6,"Yoga","Një sport qe aplikon praktike fizike, m")]
kursori.executemany(sql,val)

#Vlerat nga komnada iNSERT ti vendosen tabeles duhet perdorur commit
mydb.commit()

print(kursori.rowcount, "jane insertuar")