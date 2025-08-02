# (c) 2025 Mateus M. & Magnus S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este script contém a função utilizada para criptografar os pacotes de
    dados enviados através de requisições. A bilbioteca ```cryptography```
    permite a criptografia dos dados. A chave de criptografia deve ser
    armazenada dento do arquivo .env encontrado na raiz do projeto.

'''
#-- BIBLIOTECAS ----------------------------------------------------------
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

#-- FUNÇÕES AUXILIARES ---------------------------------------------------
def load_cipher():
    ''' Carrega a chave de criptografia do ambiente '''
    load_dotenv()

    try:
      key = os.getenv("FERNET_KEY")
    except:
      print("\33[31mUm erro ocorreu!\33[0m")
      raise

    return Fernet(key)

#-- FUNÇÕES PRINCIPAL ----------------------------------------------------
def encEncode(data:str) -> str:
    ''' Criptografa um texto '''
    cipher = load_cipher()
    return cipher.encrypt(data.encode())

def encDecode(data:str) -> str:
    ''' Descriptografa um texto '''
    cipher = load_cipher()
    return cipher.decrypt(data).decode()
#-------------------------------------------------------------------------
