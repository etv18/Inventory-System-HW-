import sqlite3

conn=sqlite3.connect('inventario.db')
c = conn.cursor()

def ShowAllStock():
    c.execute("SELECT * FROM products")
    items = c.fetchall()
    details=['id: ','Product Name: ', 'Quantity: ', 'Price: ']
    for i in range(len(items)):
        for j in range(len(items[i])):
            print(details[j],items[i][j] )
        print()
        
ShowAllStock()


conn.commit()
conn.close()