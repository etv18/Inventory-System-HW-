import sqlite3

conn=sqlite3.connect('inventario.db')
c = conn.cursor()

def ShowAllStock():
    c.execute("SELECT * FROM products")
    conn.commit()
    items = c.fetchall()
    details=['id: ','Product Name: ', 'Quantity: ', 'Price: ']
    for i in range(len(items)):
        for j in range(len(items[i])):
            print(details[j],items[i][j] )
        print()

def InsertProducts():
    print('\n--Insertando Productos--')
    id=int(input('ID del producto: '))
    name=input('Nombre del producto: ')
    price=float(input('Precio: '))
    quantity=int(input('Cantidad: '))

    newProduct={ 'id': id,
                 'name': name,
                 'quantity': quantity,
                 'price':price}
    
    c.execute('INSERT into products (id, product_name, quantity, price) VALUES (?,?,?,?)', (
               newProduct['id'], 
               newProduct['name'], 
               newProduct['quantity'], 
               newProduct['price'])
            )
    conn.commit()

def AddDiscounts():
    ShowAllStock()
    id=int(input('Ingresa el id del producto al cual deseas agregarle el descuento: '))

def AddProductsDetails():
    columnName=input('Introduce el nombre de la nueva categoria: ')
    datatype=input('Tipo del de dato (INTERGER, TEXT, REAL): ')

    c.execute(f'ALTER TABLE products ADD COLUMN {columnName} {datatype}')
    c.commit()

InsertProducts()
ShowAllStock()

conn.commit()
conn.close()