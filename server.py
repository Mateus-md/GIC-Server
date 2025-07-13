# (c) 2025 Mateus M. & Magnuss S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este script contem todas as funcionalidades de requisições HTTP.
    Todos os processos são autenticados através de um token de acesso
    definido dentro do arquivo .env para mais segurança.

'''
#-- BIBLIOTECAS ----------------------------------------------------------
from modules import *
from fastapi import FastAPI
from dotenv import load_dotenv
import os

#-- FUNÇÕES AUXILIARES ---------------------------------------------------
def is_valid(token:str) -> bool:
    ''' Valida o token de acesso informado '''
    load_dotenv()
    return os.getenv("ACCESS_TOKEN") == token

def safe_execute(db_name:str, command:str) -> None:
    ''' Exectua  um comando SQL de forma segura
    
    Args:
        db_name: O nome do banco de dados a ser acessado.
        command: Comando para ser executado.

    '''
    
    conn, cursor = cntConnectTo(db_name)

    try:
        command = conn.converter.escape(command)
        cursor.execute(command)
        conn.commit()
    except Exception as err:
        conn.roolback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        cursor.close()
        conn.close()
   
    return

#-- REQUESTS -------------------------------------------------------------
app = FastAPI()
@app.get("/new_client")
def add_client(token:str, db_name:str, nome:str, telefone:str) -> None:

    if not is_valid(token):
        raise HTTPException(status_code=401, detail="Token inválido")

    insert_command = """

    INSERT INTO gic_clientes (nome, telefone)
    VALUES (%s, %s)

    """, (nome, telefone)

    safe_execute(db_name, command=insert_command)

    return {"message": "Novo cliente adicionado!"}

@app.get("/new_vehicle")
def add_vehicle() -> None:
    return

#-------------------------------------------------------------------------
