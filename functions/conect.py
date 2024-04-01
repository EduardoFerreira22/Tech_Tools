try:
    import pyodbc
    import mysql.connector
    import sqlite3
    import psycopg2
    from PySide6.QtCore import QCoreApplication
    from PySide6.QtGui import QIcon,QFont,QColor
    from PySide6 import QtCore
    from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)
    from functions.logs import App_logs
    import os
    import uuid
except:
    pass


class Erros():
    def show_error_popup(self, error_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText("Erro ao executar a consulta:")
        msg.setInformativeText(error_message)
        msg.exec_()


class Conections_SQLServer():
    def __init__(self):

        self.cursor = None  # Inicializa o atributo cursor
        self.conn = None  # Inicializa a conexão como None
            #LOGS ----------------------------------------------------------------------------------------------------------
            # Obtém o nome do arquivo atual
        self.file_name = os.path.splitext(os.path.basename(__file__))[0] if __name__ != "__main__" else "conect"
        self.path_logs = 'logs'
        self.class_name = self.__class__.__name__
        self.log = App_logs()


    def conect_sqlserver(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        try:
            self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server +
                                  ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            
            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            return "OK"
        except Exception as e:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"conect_sqlserver Erro: {e}")
            print(e)
            return "ERRO"

class Conections_MySQL():
    def __init__(self):
        self.conn = None
        self.cursor = None
            # Obtém o nome do arquivo atual
        self.file_name = os.path.splitext(os.path.basename(__file__))[0] if __name__ != "__main__" else "conect"
        self.path_logs = 'logs'
        self.class_name = self.__class__.__name__
        self.log = App_logs()


    def MYSQL(self, host, database, username, password, port):
        try:
            # estabelece a conexão
            self.conn = mysql.connector.connect(
                user=username,
                password=password,
                host=host,
                port=port,
                database=database
            )

            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            if self.cursor:
                return "OK"

        except Exception as e:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"MYSQL Erro de conexão: {e}")
            print(f"Erro de conexão: {str(e)}")
            return "ERRO"

    def query_MySQL(self, value):
        error = Erros()
        try:
            self.cursor.execute(value)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"query_MySQL Erro de conexão: {e}")
            error.show_error_popup(str(e))
            print(f'Erro:\n{e}')

class Conections_SQLite3():   
    def __init__(self):
        self.conn = None
        self.cursor = None
            # Obtém o nome do arquivo atual
        self.file_name = os.path.splitext(os.path.basename(__file__))[0] if __name__ != "__main__" else "conect"
        self.path_logs = 'logs'
        self.class_name = self.__class__.__name__
        self.log = App_logs()


    def conectar_sqlite3_db(self, path_db):
        try:
            # Conecta-se ao banco de dados (ou cria um novo se não existir)
            self.conn = sqlite3.connect(path_db)
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida com sucesso.")
            return "OK"
        except Exception as e:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"conectar_sqlite3_db Erro ao conectar à DataBase: {e}")
            print("Erro ao conectar à DataBase:", e)
            return "ERRO"
        
        
    def query_SQLite(self, query_value):
        error = Erros()
        try:
            self.cursor.execute(f'{query_value}')
            res = self.cursor.fetchall()
                        # Recupera os nomes das colunas
            column_names = [description[0] for description in self.conn3.cursor.description]
            print(res)
            return column_names,res
        except Exception as e:
          self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"query_SQLite Erro: {e}")
          error.show_error_popup(str(e))


class Conections_PostgreSQL():
    def __init__(self):
        self.cursor = None
        self.conn = None
            # Obtém o nome do arquivo atual
        self.file_name = os.path.splitext(os.path.basename(__file__))[0] if __name__ != "__main__" else "conect"
        self.path_logs = 'logs'
        self.class_name = self.__class__.__name__
        self.log = App_logs()

    def postgresql_conect(self, host, database, username, password, port):
        
        try:
            self.conn = psycopg2.connect(dbname=database, user=username, password=password, host=host,port=port)
            self.cursor = self.conn.cursor()
            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            
            if self.cursor:
                return "OK"

        except Exception as e:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"postgresql_conect Erro de conexão: {e}")
            print(f"Erro de conexão: {str(e)}")
            return "ERRO"