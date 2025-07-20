# (c) 2025 Mateus M. & Magnus S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este script contem a função principal para acessar um banco de dados.

'''
#-- BIBLIOTECAS ----------------------------------------------------------
import mysql.connector
import os
from dotenv import load_dotenv
#-- MAIN -----------------------------------------------------------------
def cntConnectTo(db_name:str) -> tuple:
    ''' Conecta a um servidor através de um nome

    Returns:
        conn: O objeto de conexão
        cursor: O cursor de acesso à conexão

    Raises:
        Exception: Caso não seja possível acessar o banco de dados.

    '''

    load_dotenv() # Carrega as variáveis de ambiente

    try:
        conn = mysql.connector.connect(
                    user = os.getenv("DB_USER"),
                    host = os.getenv("DB_HOST"),
                    password = os.getenv("DB_PASSWORD"),
                    database = db_name
                )

    except mysql.connector.Error as err:
        print(f"\33[31mErro de conexão: {err}\33[0m")
        raise

    except Exception as err:
        print(f"\33[31mErro inesperado: {err}\33[0m")
        raise

    cursor = conn.cursor()

    # (MySQLConnector, MySQLCursor)
    return conn, cursor
#-------------------------------------------------------------------------
