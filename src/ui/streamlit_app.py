import streamlit as st
import pandas as pd
from vanna.my_vanna import MyVanna
from db.db_connection import get_connection
from config import OPENAI_API_KEY, VANNA_API_KEY, VANNA_MODEL_NAME, DB_DSN, DB_USER, DB_PASSWORD

# Inicializar Vanna
vn = MyVanna(config={
    'openai_api_key': OPENAI_API_KEY,
    'vanna_api_key': VANNA_API_KEY,
    'vanna_model_name': VANNA_MODEL_NAME,
    'db_dsn': DB_DSN,
    'db_user': DB_USER,
    'db_password': DB_PASSWORD
})

def run_streamlit():
    st.set_page_config(page_title="Consultas SQL com Vanna e OpenAI", page_icon="📝", layout="wide")
    st.title('Consultas SQL com Vanna e OpenAI')

    question = st.text_input('Digite sua pergunta:', placeholder='Ex: "Qual é o valor total dos pedidos feitos pelo cliente com ID 1?"')
    openai_question = st.text_input('Ou pergunte diretamente à OpenAI:', placeholder='Ex: "Qual é a capital da França?"')

    if st.button('Buscar Consulta SQL'):
        if question:
            try:
                # Gerar a consulta SQL usando Vanna
                sql_query = vn.ask(question)
                st.subheader("Consulta SQL Gerada")
                st.code(sql_query, language='sql')
                
                # Executar a consulta SQL
                connection = get_connection()  # Ajustado para usar get_connection diretamente
                if connection:
                    df = pd.read_sql(sql_query, connection)
                    st.subheader("Resultados da Consulta")
                    st.dataframe(df)
                    connection.close()
                else:
                    st.error("Não foi possível conectar ao banco de dados.")
            except Exception as e:
                st.error(f"Erro: {e}")

    if st.button('Buscar Resposta da OpenAI'):
        if openai_question:
            try:
                # Obter resposta da OpenAI
                openai_response = vn.get_openai_response(openai_question)
                st.subheader("Resposta da OpenAI")
                st.write(openai_response)
            except Exception as e:
                st.error(f"Erro: {e}")

if __name__ == "__main__":
    run_streamlit()
