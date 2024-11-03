# src/vanna/my_vanna.py

from vanna.custom_vector_db import CustomVectorDB  # Certifique-se de que isso reflete o que você realmente tem
from config import OPENAI_API_KEY, VANNA_API_KEY, VANNA_MODEL_NAME, DB_DSN, DB_USER, DB_PASSWORD

class MyVanna:
    def __init__(self, config=None):
        # Inicializa o Vanna com o modelo e a chave API configurados
        self.vanna = CustomVectorDB(model=config['vanna_model_name'], api_key=config['vanna_api_key'])
        self.openai_api_key = config['openai_api_key']
        self.db_dsn = config['db_dsn']
        self.db_user = config['db_user']
        self.db_password = config['db_password']
        # Aqui você pode adicionar a configuração para OpenAI se necessário

    def ask(self, question):
        # Geração de SQL usando Vanna
        return self.vanna.generate_sql(question=question)
    
    def explain(self, query):
        # Explicação do SQL usando Vanna
        return self.vanna.explain_query(query=query)

    def get_openai_response(self, question):
        # Função para obter a resposta da OpenAI
        import openai
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ajuste conforme o modelo que você está usando
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
