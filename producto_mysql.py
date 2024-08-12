import mysql.connector
from mysql.connector import Error
from datetime import datetime
from Bd_productos.producto_class import Base_de_datos

try:
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='admin93',
        db='productos',
    )
    
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM Productos')
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
except mysql.connector.Error as error:
    print("Error al conectar a la base de datos de MySQL", error)
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Conexion cerrada')
        
result = Base_de_datos('Jack', 'Nicholson', 23456343)
print(f'\nEl producto del cliente {result.Nombre} {result.Apellido} de la cedula {result.Cedula} esta:')
result = Base_de_datos.fecha(datetime(2024,8,27), datetime(2024,8,10))
print(f'{result}\n')