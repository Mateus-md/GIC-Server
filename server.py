# (c) 2025 Mateus M. & Magnus S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este script contem todas as funcionalidades de requisições HTTP.
    Todos os processos são autenticados através de um token de acesso
    definido dentro do arquivo .env para mais segurança.

'''
#-- BIBLIOTECAS ----------------------------------------------------------
from modules import *
from fastapi import FastAPI, Form, HTTPException
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
        #command = conn.converter.escape(command)
        cursor.execute(command)
        conn.commit()
    except Exception as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        cursor.close()
        conn.close()

    return

def decrypt( pipe:str = Form(...) ) -> dict:
    ''' Transforma um pacote em um formato desejado '''
    try:
      package = encDecode(pipe)
      data = cnvFormat(package)
    except:
      raise HTTPException(status_code=401, detail="Não autorizado!")
    return data

#-- REQUISIÇÕES ----------------------------------------------------------
app = FastAPI()

# Cadastro de clientes
@app.post("/novo_cliente")
async def add_client( pipe:str = Form(...) ) -> dict:
    ''' Cadastra um novo cliente '''

    data = decrypt(pipe)

    if not is_valid( data["token"] ):
      raise HTTPException(status_code=401, detail="Token inválido!")

    insert_command = f"""
      INSERT INTO gic_clientes (nome_cliente, telefone)
      VALUES ("{data['nome_cliente']}", "{data['telefone']}")
    """
    safe_execute(data["db_name"], command=insert_command)

    return {"status_code":200,"message":"Novo cliente cadastrado!"}

# Cadastro de serviços
@app.post("/novo_serviço")
async def add_service( pipe:str = Form(...) ) -> dict:
    ''' Cadastra um novo serviço  '''

    data = decrypt(pipe)

    if not is_valid( data["token"] ):
      raise HTTPException(status_code=401, detail="Token inválido!")

    insert_command = f"""
      INSERT INTO gic_servicos (tipo_servico, valor_servico)
      VALUES ("{data['tipo_servico']}", {data['valor_servico']})
    """
    safe_execute(data['db_name'], command=insert_command)

    return {"status_code":200, "message":"Novo serviço cadastrado!"}
#-------------------------------------------------------------------------
