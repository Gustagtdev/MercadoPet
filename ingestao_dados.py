import requests
from dotenv import load_dotenv
import os
import re # Pacote de expressões regulares para manipulação de strings
import pandas as pd

load_dotenv()
dog_api_key = os.getenv("DOG_API_KEY")

url = "https://api.thedogapi.com/v1/breeds"
headers={"x-api-key": dog_api_key}

response = requests.get(url,headers=headers)

print(response.status_code) # Deu 200: Requisição bem sucedida
data = response.json()
# print(type(data)) #Tipo de Estrutura de Dados: Lista a API retorna uma lista de raças
# print(len(data)) # Retorna o número de elementos em uma Estrutura de Dados: Tem 631 raças cadastradas na API
# print(data[0].keys()) # Retorna as chaves do primeiro elemento do dicionário: cada raça é representada por um dicionário com várias chaves
# print(data[0]["name"]) # Retorna o valor da chave "name" do primeiro elemento do dicionário: Confirma que dá pra acessar campos específicos


# Criando um DataFrame a partir da lista de raças
df = pd.DataFrame(data)
colunas_uteis = ["id", "name", "breed_group", "life_span", "temperament", "origin","weight", "height", "image"]
df = df[colunas_uteis]
print(df.head()) # Mostra as primeiras linhas do DataFrame
print(df.info()) # Mostra informações sobre o DataFrame, como número de linhas, colunas e tipos de dados
