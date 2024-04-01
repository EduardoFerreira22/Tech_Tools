import sys
import fdb


# Dados de conexão
hostname = 'localhost'
database = 'F:\\Resulth Emissor NFE\\RESULTH.FB'
user = 'SYSDBA'
password = 'masterkey'

# Realizar a conexão
conn = fdb.connect(
    host=hostname,
    database=database,
    user=user,
    password=password,
    charset='utf-8'
)

# Criar um cursor para executar consultas SQL
cur = conn.cursor()

# Consulta para obter a lista de tabelas
cur.execute("SELECT rdb$relation_name FROM rdb$relations WHERE rdb$view_blr IS NULL AND (rdb$system_flag IS NULL OR rdb$system_flag = 0)")

# Ler os resultados
tables = [row[0] for row in cur.fetchall()]

# Exibir a lista de tabelas
print("\nLista de tabelas:")
for table in tables:
    print(table)


conn.close()
