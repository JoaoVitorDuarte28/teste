import pyodbc
import _json
server = '10.100.100.5' 
database = 'dbSicred_Proj' 
username = 'usr_sicred' 
password = '#Homologsicr3d#' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
   
#Sample select query
cursor.execute("select situacao, DESCRICAO from PROPOSTASSITUACAO") 
rows = cursor.fetchall()
teste = tuple(rows)
print(teste)