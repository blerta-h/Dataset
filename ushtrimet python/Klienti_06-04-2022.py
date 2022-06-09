import os
import platform
import mysql.connector
import pandas as pd

#lidhjen me databaze
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "QPALzm12.",
    database = "ushqimi_projekt_bigdata1"
)

kursori = mydb.cursor()
#definojme funksionin Klienti
#definojme funksionin Klienti
def Klienti():
	L=[]
	Klienti_id = int(input("Shkruani ID e Klientit: "))
	L.append(Klienti_id)
	Klienti_emri = input("Shkruani EMRIN e Klientit: ")
	L.append(Klienti_emri)
	Klienti_nrtelefonit = input("Shkruani NUMRIN E TELEFONIT te Klientit: ")
	L.append(Klienti_nrtelefonit)
	Pagesa = int(input("Shkruani PAGESEN e Klientit: "))
	L.append(Pagesa)
	Statusi_pageses = input("Shkruani STATUSIN E PAGESES se Klientit: ")
	L.append(Statusi_pageses)
	Email = input("Shkruani EMAIL e Klientit: ")
	L.append(Email)
	Porosia_id = input("Shkruani ID E POROSISE se Klientit: ")
	L.append(Porosia_id)
	Puntori_id = input("Shkruani ID E PUNTORIT: ")
	L.append(Puntori_id)
	Data = input("Shkruani DATEN e Porosise: ")
	L.append(Data)
	cust=(L)
	sql_query = "INSERT INTO Klienti(Klienti_id,Klienti_emri,Klienti_nrtelefonit,Pagesa,Statusi_pageses,Email,Porosia_id,Puntori_id,Data) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	kursori.execute(sql_query, cust)
	mydb.commit()