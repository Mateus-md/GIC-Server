## Visão Geral
**GIC-Server** é uma aplicação de servidor backend projetada para gerenciar e lidar com operações de um sistema de controle de clientes.
Ela fornece endpoints de API para aplicações clientes e processa requisições de forma modular.

> **Nota**: Este repositório está em desenvolvimento ativo. Funcionalidades, endpoints e estruturas estão sujeitos a alterações.

## Instalação
1. Clone o repositório:
  ```bash
  git clone https://github.com/Mateus-md/GIC-Server.git
  cd GIC-Server
  ```

2. Instale as depedências:
  ```bash
  pip install -r requirements.txt
  ```

3. Configure as variáveis de ambiente em um arquivo .env:
  ```bash
  # Estrutura de exemplo
  DB_USER = seu_mysql_username
  DB_HOST = seu_host_IP # geralmente 'localhost'
  DB_PASSWORD = sua_senha
  ACCESS_TOKEN = qualquer_token_de_acesso
  ```

## Utilização
Para utilizar o serviço, simplemente rode o servidor através do comando:
  ```bash
  uvicorn server:app --host 0.0.0.0 --port 8000
  ```

As requisições são feitas através do protocólo HTTP em http://<SERVER.IP>:8000/

## Contato
Este repositório é mantido por [Mateus Moreira](https://github.com/Mateus-md).

## License
This project is licensed under the MIT License. See LICENSE for details.
