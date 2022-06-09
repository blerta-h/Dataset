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
def Puntori():
	L=[]
	Puntori_id = int(input("Shkruani ID e Puntorit: "))
	L.append(Puntori_id)
	Puntori_emri = input("Shkruani EMRIN e Klientit: ")
	L.append(Puntori_emri)
	Puntori_mosha = input("Shkruani NUMRIN E TELEFONIT te Klientit: ")
	L.append(Puntori_mosha)
	Puntori_nrtelefonit = int(input("Shkruani PAGESEN e Klientit: "))
	L.append(Puntori_nrtelefonit)
	Passwordi = input("Shkruani STATUSIN E PAGESES se Klientit: ")
	L.append(Passwordi)
	pun=(L)
	sql_query = "INSERT INTO Puntori(Puntori_id,Puntori_emri,Puntori_mosha,Puntori_nrtelefonit,Passwordi) VALUES (%s,%s,%s,%s,%s)"
	kursor.execute(sql_query, pun)
	mydb.commit()