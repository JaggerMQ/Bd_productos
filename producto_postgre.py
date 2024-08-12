import psycopg2
from Bd_productos.producto_class import Base_de_datos
from datetime import datetime

try:
    
    conn = psycopg2.connect(
        user='postgres',
        host='localhost',
        database='Productos',
        port='5432',
        password='admin93'
    )
    
    cursor = conn.cursor()
    
    cursor.execute('''SELECT Nombre, Cedula, Compra, Vence FROM Productos''')
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print('Error al conectar a la base de datos', error)
    
finally:
    if conn:
        cursor.close()
        conn.close()
        print('Conexion cerrada')
        

result = Base_de_datos('Jack', 'Nicholson', 23543654)
print(f'\nEl producto del cliente {result.Nombre} {result.Apellido} de la cedula {result.Cedula} esta:')
result = Base_de_datos.fecha(datetime(2024,9,20), datetime(2024,7,15))
print(f'{result}\n')