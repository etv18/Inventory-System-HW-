import sqlite3

conn = sqlite3.connect('inventario.db')
c = conn.cursor()

stock=[
   {'id': 1 , 
    'name': 'Leche Milex', 
    'price': 75.99, 
    'quantity':20}, 

   {'id': 2 , 
    'name': 'Carton de Huevos', 
    'price': 204.99, 
    'quantity':50},

   {'id': 3 , 
    'name': 'Saco de Arroz 10lb', 
    'price': 299.99, 
    'quantity':17}
]

discounts={
    3: 0.10, # <----10%
    1: 0.3 # <----30%
}

#Creating products table
c.execute("""
        CREATE TABLE products (
          id INTERGER,
          product_name TEXT,
          quantity INTERGER,
          price REAL
        )
""")

conn.commit()


for item in stock:
    c.execute('INSERT into products (id, product_name, quantity, price) VALUES (?,?,?,?)',
              (item['id'],
               item['name'], 
               item['quantity'],
               item['price'])
            )



conn.commit()
conn.close()