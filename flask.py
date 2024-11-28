import sqlite3


dok = sqlite3.connect("Artistc.db") #Create
cursor = dok.cursor()

cursor.execute("SELECT * FROM artists")#Select
data = cursor.fetchall()
print(len(data))

cursor.execute("SELECT * FROM artists WHERE gender=='Female'")
data = cursor.fetchall()
print(len(data))
dok.commit()

cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print(len(data))
dok.commit()

cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900 order by "Birth Year"')
data = cursor.fetchall()
print(data[0][0])
dok.commit()





#cursor.execute()#Delete
#dok.commit()

#dok.close()

