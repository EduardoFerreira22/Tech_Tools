from functions.conect import Conections_SQLServer,Conections_MySQL
import  pyodbc



import subprocess
import os


conn = Conections_SQLServer()
resp = conn.conect_sqlserver('TECHTOOLS\\MUNDO','Hiper','sa','mundo')

def listar_databases_sql_server(server, user, password):
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';UID='+user+';PWD='+password)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
        databases = [database[0] for database in cursor.fetchall()]
        print(databases)
        return databases
    except pyodbc.Error as err:
        print("Erro ao conectar ao SQL Server:", err)
        return []
listar_databases_sql_server('TECHTOOLS\\MUNDO','sa','mundo')
"""def realizar_backup(tipo_banco, nome_banco, usuario, senha, caminho_destino):
    if tipo_banco.lower() == 'sqlserver':
        comando_backup = f'sqlcmd -S techtools\\mundo -d {nome_banco} -U {usuario} -P {senha} -Q "BACKUP DATABASE {nome_banco} TO DISK=\'{caminho_destino}\\{nome_banco}.bak\'"'
    elif tipo_banco.lower() == 'mysql':
        comando_backup = f'mysqldump -u {usuario} -p{senha} {nome_banco} > {caminho_destino}\\{nome_banco}.sql'
    else:
        print("Tipo de banco de dados inválido.")
        return

    try:
        subprocess.run(comando_backup, shell=True, check=True)
        print("Backup realizado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao realizar o backup: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

type_db = 'sqlserver'
db = 'Hiper'
usa = 'sa'
pwd = 'mundo'
path = 'C:\\Hiper'
realizar_backup(type_db, db, usa, pwd, path)
"""