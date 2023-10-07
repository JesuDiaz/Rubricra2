import pyodbc

# Configuración de la conexión a la base de datos Access
connection = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\alexa\Documents\Documentos U Jesús\BPDS 2023-2\myprojectweb\app\TaskBD.accdb;'
)

cursor = connection.cursor()