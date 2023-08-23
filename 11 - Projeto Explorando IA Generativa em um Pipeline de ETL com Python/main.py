import openai
import pandas as pd
import requests
import os
from dotenv import load_dotenv

#Extração de dados da API da DevWeek
sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"

df = pd.read_csv('C:\\Users\\Nathan Fontenele\\Documents\\BootcampSantander2023\\11 - Projeto Explorando IA Generativa em um Pipeline de ETL com Python\\SDW2023.csv')

user_ids = df['UserID'].to_list()

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

#Transformação ou Enriquecimento de dados através da API da OpenAi
load_dotenv()
openai.api_key = os.getenv("API_KEY")

def generate_ia_news(user):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em T.I"
        },
        {
            "role": "user",
            "content": f"Crie relatório para {user['name']} de máquinas ativas (máximo 400 caracteres.)"
        }
    ]
    )
    return completion.choices[0].message.content.stripe('\"')

for user in users:
    news = generate_ia_news(user)
    user['news'].append({
        "icon": "",
        "description": news
    })
    print(news)

#Carregamento dos dados na API da DevWeek
def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    sucess = update_user(user)
    print(f"Atualizado: {sucess}")