import sqlite3
connection = sqlite3.connect('gta.db')
cursor=connection.cursor()
cursor.execute('create table gta(release_year integer,release_make text,country text,release_hp integer)')


release_list = [
    (1997,'ford','yellow', 4),
    (1998,'toyota','blue',20),
    (1999,'mercedes','green',18),
    (2000,'jeep','red',16)
]
cursor.executemany('insert into gta values (?, ?, ?,?)',release_list)
for row in cursor.execute('select * from gta'):
    print(row)
print('----------------------')
cursor.execute('select * from gta where country =:c',{'c':'country'})
gta_search = cursor.fetchall()
print('gta_search')

connection.close()