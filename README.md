## Objetivo

Construir um projeto de portfólio voltado ao mercado pet, usando **dados públicos via API**, com o objetivo de demonstrar uma stack completa de **Data Engineering**: ingestão de dados, tratamento, modelagem, carga em banco relacional e visualização em BI.

O projeto foi pensado especificamente para reforçar a transição de carreira de Análise de Dados/BI para **Data Engineering**, indo além de um dashboard puro em cima de um CSV estático.

## Decisões tomadas

- Fonte de dados: **APIs públicas** (não Kaggle/CSV estático), para simular ingestão contínua/programática
- API escolhida para o início: **The Dog API** (`https://api.thedogapi.com`)
- Autenticação: chave de API armazenada em `.env` (via `python-dotenv`), nunca exposta no código
- Execução dos scripts: `python nome_do_arquivo.py` (não usar `m` com extensão `.py`)

## Roteiro do projeto (visão geral)

1. **Consumir a API** — requisições HTTP com `requests`, entendendo autenticação (header) e o formato da resposta (JSON)
2. **Tratar e explorar os dados** — transformar o JSON em DataFrame (`pandas`), entender tipos de dados e valores ausentes
3. **Modelar em esquema estrela** — definir tabelas fato e dimensão a partir dos dados da API
4. **Criar o banco e as tabelas** — escrever o DDL em PostgreSQL refletindo o modelo estrela
5. **Carregar os dados no banco** — inserir os dados tratados via Python (`psycopg2` ou `SQLAlchemy`)
6. **Automatizar a ingestão** — rodar o script periodicamente, com lógica de upsert (evitar duplicação)
7. **Conectar o Power BI** — construir o dashboard final direto sobre o banco PostgreSQL, não sobre CSV
