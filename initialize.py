# (c) 2025 Mateus M. & Magnus S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este srcipt é utilizado para criar todas as tabelas necessárias
    dentro de um banco de dados. As tabelas são criadas dentro do banco
    apenas se o banco não tiver uma tabela com o mesmo nome. Assim,
    este script pode ser executado para verificar a integridade de um
    banco de dados também.

    O script deve ser executado apenas quando necessário e não é utilizado
    fora do uso de criação e verificação de um banco de dados.

    Para usa-lo, primeiro certifique-se de que haja um banco de dados
    MySQL criado e que as autenticações necessárias estejam presentes
    dentro do arquivo .env localizado na raiz do projeto.
    Em seguida, execute este script:

    ```bash
    python3 initialize.py
    ```

    Informe o nome do banco criado. Logo após, uma mensagem deve informar
    que a estrutura do banco foi devidamente inicializada.

'''
#-- BIBLIOTECAS ----------------------------------------------------------
import mysql.connector
from fastapi import FastAPI
from modules import *
#-- MAIN -----------------------------------------------------------------
def initialize(database_name:str) -> None:
    ''' Função principal - Cria um banco e suas tabelas '''

    conn, cursor = cntConnectTo(database_name)

    try: # Cria novas tabelas

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS gic_clientes(
                            id_cliente      INTEGER AUTO_INCREMENT PRIMARY KEY,
                            nome_cliente    VARCHAR(255) NOT NULL,
                            telefone        CHAR(12) UNIQUE
                        );
                        CREATE TABLE IF NOT EXISTS gic_cpf(
                            num_cpf         CHAR(14) PRIMARY KEY,
                            id_cliente      INTEGER NOT NULL,
                            FOREIGN KEY (id_cliente) REFERENCES gic_clientes(id_cliente)
                        );
                        CREATE TABLE IF NOT EXISTS gic_cnpj(
                            num_cnpj        CHAR(18) PRIMARY KEY,
                            id_cliente      INTEGER NOT NULL,
                            FOREIGN KEY (id_cliente) REFERENCES gic_clientes(id_cliente)
                        );
                        CREATE TABLE IF NOT EXISTS gic_veiculos(
                            placa           VARCHAR(7) PRIMARY KEY,
                            id_cliente      INTEGER NOT NULL,
                            tipo_veiculo    VARCHAR(255) NOT NULL,
                            observacoes     LONGTEXT,
                            FOREIGN KEY (id_cliente) REFERENCES gic_clientes(id_cliente)
                        );
                        CREATE TABLE IF NOT EXISTS gic_enderecos(
                            id_cliente       INTEGER NOT NULL,
                            rua              VARCHAR(255) NOT NULL,
                            num              INTEGER NOT NULL,
                            bairro           VARCHAR(255) NOT NULL,
                            cidade           VARCHAR(255) NOT NULL,
                            estado           CHAR(2) NOT NULL,
                            complemento      VARCHAR(255),
                            FOREIGN KEY (id_cliente) REFERENCES gic_clientes(id_cliente)
                        );
                        CREATE TABLE IF NOT EXISTS gic_servicos(
                            id_servico      INTEGER AUTO_INCREMENT PRIMARY KEY,
                            tipo_servico    VARCHAR(255) NOT NULL UNIQUE,
                            valor_servico   FLOAT DEFAULT 0
                        );
                        CREATE TABLE IF NOT EXISTS gic_servicos_encerrados(
                            id_os           INTEGER AUTO_INCREMENT PRIMARY KEY,
                            id_servico      INTEGER NOT NULL,
                            id_cliente      INTEGER NOT NULL,
                            data            DATE NOT NULL,
                            horario         TIME NOT NULL,
                            valor_servico   FLOAT DEFAULT 0,
                            FOREIGN KEY (id_servico) REFERENCES gic_servicos(id_servico),
                            FOREIGN KEY (id_cliente) REFERENCES gic_clientes(id_cliente)
                        )
                       """)
        # conn.commit()

    except Exception as err:
        print(f"\33[31mErro inesperado: {err}\33[0m")
        raise

    finally:
        cursor.close()
        conn.close()

    return
#-------------------------------------------------------------------------
if __name__ == "__main__":
    db = input("Nome do banco >> ")
    try:
      if db: initialize(db)
      print("\33[32mA estrutura do banco foi criada!\33[0m")
    except:
      print("\33[31mUm erro ocorreu durante a inicialização\33[0m")
      raise
