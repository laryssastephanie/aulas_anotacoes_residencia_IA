import pymssql
import pandas as pd

conn = pymssql.connect(server='192.168.65.141', user='ResidenciaIA', password='Hub_Sicoob@2021', database='DataStage')

cursor = conn.cursor()

cursor.execute('SELECT * from clc.REUNIOESCOPOM')

data = cursor.fetchall()

df=pd.DataFrame(data)

print(df)

cursor.close()

