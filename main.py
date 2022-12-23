from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import _json
import pyodbc
server = '10.100.100.5' 
database = 'dbSicred_Proj' 
username = 'usr_sicred' 
password = '#Homologsicr3d#' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.put("/alterar/Status")
def read_item(numeroProposta: int, numeroSituacao:int):
    cursor.execute("EXEC PR_UPD_PROPOSTASCREDITO {} , '{}', 'PROPOSTASCREDITO'".format(numeroProposta, numeroSituacao))
    cnxn.commit()
    return {"Proposta Alterada"}


@app.get("/consulta/proposta")
def consulta(numeroProposta: int):
    cursor.execute("select situacao from propostascredito where proposta = {}".format(numeroProposta))
    resultado = cursor.fetchone()
    numProposta = list(resultado)
    return numProposta




@app.get("/consulta")
def consulta():
    cursor.execute("select situacao, DESCRICAO from PROPOSTASSITUACAO")
    resultado = cursor.fetchone()
    teste = tuple(resultado)
    print(resultado)
    return teste
