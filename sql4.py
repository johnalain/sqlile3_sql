#read data from the table
import sqlite3
from tkinter.tix import Select
db = sqlite3.connect('movies.db')
cur = db.cursor()
# data = cur.execute("SELECT rowid,* FROM movie ORDER BY year ASC LIMIT 3")
#ORDER BY title sort column from a to z u can use by genre by year also if u add DESC "ASC by default arrangement" after ORDER BY year will reverse the sort 
#if i put rowid instead of * will add id column auto incremented "rowid, *"will print all with id
#if u add LIMIT after DESC wirh number of rows
# u can select what u want data u want to recall from "data = cur.execute(select .....)"command

# for row in data: 
#  print (row[0])
# print(cur.fetchone())
#fetchone() will print 1st  row
# print(cur.fetchmany(2))
#fetchmany(number of lines in list )
data = cur.execute("SELECT rowid,* FROM movie WHERE title = 'oppenheimer'")
#WHERE is to add condition to display matching data the condition here is (title = 'oppenheimer')
data = (cur.fetchall())
for row in data:
    print(row)
#u can put index in row[0 or 1 or 2 or 3 ]
#print all rows in a list
# #print all table
 #print(row[0]) print all title[1]print genre[2]print year when i add rowid print (row[0])wil print id column
db.commit()
db.close()
#time:36:25