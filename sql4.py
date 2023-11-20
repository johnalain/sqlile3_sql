#read data from the table
import sqlite3
from tkinter.tix import Select
db = sqlite3.connect('movies.db')
cur = db.cursor()
data = cur.execute("SELECT  * FROM movie")

for row in data: 
 print (row)#print all table
 #print(row[0]) print all title[1]print genre[2]print year
 db.commit()
db.close()
#time:24:49