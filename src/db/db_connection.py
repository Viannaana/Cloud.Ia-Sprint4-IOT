import jaydebeapi

def get_connection():
    # Caminho para o driver JDBC
    jdbc_driver_name = "oracle.jdbc.driver.OracleDriver"
    jdbc_driver_loc = "/Users/anajuliavianna/Downloads/ojdbc8.jar"
    
    # URL de conexão
    jdbc_url = "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl"
    
    # Credenciais
    user = "RM98974"
    password = "100903"
    
    # Conexão com o banco de dados
    connection = jaydebeapi.connect(
        jdbc_driver_name,
        jdbc_url,
        [user, password],
        jdbc_driver_loc
    )
    
    return connection
