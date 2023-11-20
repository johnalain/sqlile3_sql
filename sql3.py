#insert row into table
import sqlite3
from tkinter.tix import INTEGER, TEXT
from turtle import title
con = sqlite3.connect('movies.db')
cursor = con.cursor()
movies = [
    ('the godfather','crime',1970),
    ('oppenheimer','drama',2023),
    ('the whale','drama',2023),
    ('delete history','comedy',2023),
    ('apples','fantasy',2020),
    ('nomadeland','drama',2020),
]
# cursor.execute("INSERT INTO movie (title,genre) VALUES('opeheimer','drama')")
#another method
# cursor.execute("INSERT INTO movie  VALUES('opeheimer','drama',2013)")
cursor.executemany("INSERT INTO movie  VALUES(?,?,?)",movies)#time:16:12 https://youtu.be/Ykf5zxBMxZ8
con.commit()
con.close()