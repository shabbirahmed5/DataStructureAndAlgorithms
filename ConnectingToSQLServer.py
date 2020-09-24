import pyodbc as db

conn = db.connect('Driver={SQL Server};'
                      'Server=########;'
                      'Database =########;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

data = cursor.execute('Select * from KPI_REPORTING_DB.dbo.Material_Extension_Tracker')

for i in data:
    print(i)
