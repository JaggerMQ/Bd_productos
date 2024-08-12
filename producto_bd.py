import sqlite3
from datetime import datetime
from Bd_productos.producto_class import Base_de_datos

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''SELECT Nombre, Apellido, Cedula FROM Productos''')
rows = cursor.fetchall()

for row in rows:
    print(f'{row}')

conn.close()

result = Base_de_datos('Jack', 'Nicholson', 23543654)
print(f'\nEl producto del cliente {result.Nombre} {result.Apellido} de la cedula {result.Cedula} esta:')
result = Base_de_datos.fecha(datetime(2024,8,20), datetime(2024,8,12))
print(f'{result}\n')