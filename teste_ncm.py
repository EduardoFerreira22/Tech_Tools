from functions.conect import Conections_SQLServer,Conections_MySQL



import subprocess
import os


conn = Conections_SQLServer()
resp = conn.conect_sqlserver('TECHTOOLS\\MUNDO','Hiper','sa','mundo')

def realizar_backup(tipo_banco, nome_banco, usuario, senha, caminho_destino):
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
