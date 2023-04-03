#!/usr/bin/env python
# coding: utf-8

# In[1]:


#koneksi
import mysql.connector

#conec dari server
conn = mysql.connector.connect(host = "localhost", user = "root", password = "")

print(conn)

#disconec dr server
conn.close()


# In[4]:


#create database
import mysql.connector

dataBase=mysql.connector.connect(host = "localhost", user = "root", password = "")

#prepar obj
cursorObj=dataBase.cursor()

#create db
cursorObj.execute("CREATE DATABASE D3_TI_2023")


# In[5]:


#Tabel mahasiswa
import mysql.connector

dataBase = mysql.connector.connect(host = "localhost", user = "root", password = "", database="D3_TI_2023")

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
mhsRecord = """CREATE TABLE tabel_mahasiswa(NIM VARCHAR(10)NOT NULL PRIMARY KEY, NAMA VARCHAR(30) NOT NULL, 
                ALAMAT VARCHAR(255), MATKUL_YANG_DIIKUTI VARCHAR(10) NOT NULL)"""

#table create
cursorObj.execute(mhsRecord)

#disconec
dataBase.close()


# In[6]:


#Tabel dosen
import mysql.connector

dataBase = mysql.connector.connect(host = "localhost", user = "root", password = "", database="D3_TI_2023")

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
dosenRecord = """CREATE TABLE tabel_dosen(NIP VARCHAR(20)NOT NULL PRIMARY KEY, NAMA VARCHAR(50) NOT NULL, 
                MATKUL_YG_DIAJAR VARCHAR(50) NOT NULL)"""

#table create
cursorObj.execute(dosenRecord)

#disconec
dataBase.close()


# In[7]:


#Tabel mata kuliah
import mysql.connector

dataBase = mysql.connector.connect(host = "localhost", user = "root", password = "", database="D3_TI_2023")

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
mkRecord = """CREATE TABLE tabel_matkul(kode_MK VARCHAR(10)NOT NULL PRIMARY KEY, nama_MK VARCHAR(50) NOT NULL, 
                WAKTU DATE, RUANG VARCHAR(10))"""

#table create
cursorObj.execute(mkRecord)

#disconec
dataBase.close()


# In[9]:


#insert data mahasiswa
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()

sql="INSERT INTO tabel_mahasiswa(NIM, NAMA, ALAMAT, MATKUL_YANG_DIIKUTI) VALUES(%s,%s,%s,%s)"
val = [("V3922001","Alexa","Solo","Wirelles"),
("V3922002","Kevin","Jakarta","Mikrokontroller"),
("V3922003","Zifa","Madiun","Kewirausahaan"),
("V3922004","Naya","Ponorogo","Etika Kerja"),
("V3922005","Agsa","Surabaya","Python")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[12]:


#insert data dosen
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()

sql="INSERT INTO T_Dosen(NIP, NAMA, MATKUL_YG_DIAJAR) VALUES(%s,%s,%s)"
val = [("0011","Yusuf Fadlila","Python"),
("0012","Darmawan","Kewirausahaan"),
("0013","Kanthi","Etika Kerja"),
("0014","Fendi","Mikrokontroller"),
("0015","Yusuf","Wirelles")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[2]:


#insert data matkul
import mysql.connector


dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()


sql="INSERT INTO tabel_matkul(kode_MK, nama_MK, WAKTU, RUANG) VALUES(%s,%s,%s,%s)"
val = [("6601","Etika Kerja","2023-4-3","L2R2"),
       ("6602","Kewirausahaan","2023-4-4","L1R2"),
       ("6603","Python","2023-4-5","Ruang Mikro"),
       ("6604","Wirelles","2023-4-6","Aula"),
       ("6605","Mikrokontroller","2023-4-7","Ruang L1R1 ")]


cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[4]:


#menampilkan data
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023") #membuka database

#preparing a cursor object
cursorObj = dataBase.cursor()

sql = "SELECT NAMA, MATKUL_YG_DIAJAR FROM tabel_dosen"

cursorObj.execute (sql)

myresult = cursorObj.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




