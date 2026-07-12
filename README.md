Projeto Price Watcher

                 +----------------+
                 | monitor_service|
                 +-------+--------+
                         |
                         ▼
                 +---------------+
                 |store_resolver |
                 +-------+-------+
                         |
               +---------+---------+
               |                   |
               ▼                   ▼
         Amazon Service      Mercado Livre
               |
         +-----+------+
         |            |
         ▼            ▼
      Client       Parser
               |
               ▼
            SQLite
               |
               ▼
           Telegram

Esse projeto não tem foco comercial. Seu foco é 100% estudo prático.
O projeto consiste no monitoramento de preços em e-commerces, a ideia é que o usuário possa cadastrar um produto de determinada loja e receber alertas caso o preço abaixe e um alerta especial caso atinja um valor estipulado pelo usuário como preço alvo.
Fluxo completo:
O usuário cadastra o produto utilizando a URL e define um preço alvo
                        ⬇️
Através da URL, o sistema identifica o e-commerce que será monitorado
                        ⬇️
O sistema busca as informações do produto (Utilizando scraper ou consumindo API do e-commerce)
                        ⬇️
Os dados do produto são gravados no banco. (Persistencia de dados)
                        ⬇️
Periodicamente, o produto é consultado novamente ➡️ Caso não o preço não tenha sido alterado, para e vai para o próximo produto
                        ⬇️
Caso o preço tenha sido alterado, a nova consulta é gravada no banco de dados. (Persistencia de dados)
                        ⬇️
Se o preço for menor que o anterior, envia uma mensagem ao usuário informando o valor (Ou uma mensagem especial caso preço do produto <= preço alvo).

A ideia é utilizar na prática conceitos de Python e persistencia de dados.

Status do projeto:
⚒️Em desenvolvimento
Funcionalidades implementadas:
✔ Persistência SQLite

✔ Arquitetura modular

✔ Logging

✔ Integração Amazon

🚧 Monitoramento automático

🚧 Telegram

🚧 Agendamento das consultas

Tecnologias

- Python
- SQLite
- BeautifulSoup
- curl_cffi
- python-dotenv
- python-telegram-bot
- schedule
