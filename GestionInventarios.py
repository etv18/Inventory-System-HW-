import sqlite3

conn=sqlite3.connect('inventario.db')
c=conn.cursor()


conn.commit()
conn.close()