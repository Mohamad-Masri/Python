import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=databade_name;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.exute('SELECT * FROM database_name.table')

for row in cursor:
    print(row)
