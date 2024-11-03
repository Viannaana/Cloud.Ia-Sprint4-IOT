import vanna
from db.db_connection import get_connection
import os

# Função para ler o DDL dos arquivos
def load_ddl_from_files(directory):
    ddl_statements = ""
    for filename in os.listdir(directory):
        if filename.endswith(".sql"):
            with open(os.path.join(directory, filename), 'r') as file:
                ddl_statements += file.read() + "\n"
    return ddl_statements

# Configurar o cliente Vanna
def setup_vanna():
    connection = get_connection()
    vanna_client = vanna.VannaDefault(api_key='YOUR_API_KEY')  # Substitua pelo seu API key
    
    # Carregar DDL dos arquivos na pasta 'ddl'
    ddl_directory = 'src/db/ddl'
    ddl_statements = load_ddl_from_files(ddl_directory)
    
    # Treinar o modelo com o DDL carregado
    if ddl_statements:
        vanna_client.train(ddl=ddl_statements)
    
    # Treinar o modelo com as queries
    query_file = 'src/db/queries.py'
    if os.path.exists(query_file):
        with open(query_file, 'r') as file:
            queries = file.read()
            vanna_client.train(sql=queries)
    
    return vanna_client

# Função principal para configurar e treinar o modelo
def main():
    vanna_client = setup_vanna()
    print("Modelo Vanna configurado e treinado com sucesso.")

if __name__ == "__main__":
    main()
