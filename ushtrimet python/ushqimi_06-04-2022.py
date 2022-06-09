import os
import platform
import mysql.connector
import pandas as pd
#lidhjen me databaze
mydb = mysql.connector.connect(
	host="localhost",
	user= "root",
	password= "QPALzm12.",
	database="ushqimi_projekt_bigdata1"
	)
kursor = mydb.cursor()
#definojme funksionin Puntori
def Ushqimi():
	L=[]
	Ushqimi_id = int(input("Shkruani ID e Puntorit: "))
	L.append(Ushqimi_id)
	Ushqimi_emri = input("Shkruani EMRIN e Klientit: ")
	L.append(Ushqimi_emri)
	Ushqimi_sasia = input("Shkruani NUMRIN E TELEFONIT te Klientit: ")
	L.append(Ushqimi_sasia)
	Qmimi = int(input("Shkruani PAGESEN e Klientit: "))
	L.append(Qmimi)
	ushq=(L)
	sql_query = "INSERT INTO Ushqimi(Ushqimi_id,Ushqimi_emri,Ushqimi_sasia,Qmimi) VALUES (%s,%s,%s,%s)"
	kursor.execute(sql_query, ushq)
	mydb.commit()