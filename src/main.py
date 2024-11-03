from vanna.my_vanna import MyVanna
from db.ddl_statements import ddl_statements
from db.queries import queries
from config import OPENAI_API_KEY, VANNA_API_KEY, VANNA_MODEL_NAME, DB_DSN, DB_USER, DB_PASSWORD
from db.db_connection import get_connection


def setup_vanna():
    global vn
    # Passar as configurações diretamente para o MyVanna
    vn = MyVanna(config={
        'openai_api_key': OPENAI_API_KEY,
        'vanna_api_key': VANNA_API_KEY,
        'vanna_model_name': VANNA_MODEL_NAME,
        'db_dsn': DB_DSN,
        'db_user': DB_USER,
        'db_password': DB_PASSWORD
    })
    connect_and_train_model()

def connect_and_train_model():
    # Conectar ao Oracle
    connection = get_connection()  # Usa a função de conexão
    if connection:
        # Configurar a conexão no Vanna
        vn.connect_to_oracle(dsn=DB_DSN, user=DB_USER, password=DB_PASSWORD)
        
        # Adicionar DDL
        for ddl in ddl_statements:
            vn.train(ddl=ddl)
        
        # Adicionar queries
        for query in queries:
            vn.train(sql=query['sql'])
        
        connection[0].close()  # Fechar a conexão
    else:
        print("Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    setup_vanna()
