import fdb

# Defina os parâmetros de conexão
hostname = 'localhost'
database = 'E:\\Backup main\\Documentos\\Perseu\\server\\BD\\BASE.FDB'
user = 'SYSDBA'
password = 'masterkey'

# Tente se conectar ao banco de dados
try:
    conn = fdb.connect(host=hostname, database=database, user=user, password=password)
    print("Conexão bem-sucedida!")
    
    # Execute consultas ou operações no banco de dados aqui
    
    # Não se esqueça de fechar a conexão quando terminar
    conn.close()
    
except fdb.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
