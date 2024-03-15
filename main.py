from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)
from ui_main import Ui_MainWindow,UI_LoginWindow
from processarmento import Processing_CSV
from win_result import SQLWindown
from functions.conect import Erros
from functions.data import SQLite_Data
from functions import conect
from openpyxl import Workbook
import subprocess
from datetime import datetime
import sqlite3
import psycopg2
import zipfile
import requests
from tqdm import tqdm
import psutil
import pyodbc
import bcrypt
import time
import json
import csv
import sys
import os
import re


    #REALIZA A BUSCA POR SERVIDORES DE BANCO DE DADOS ATIVOS NO MOMENTO.
def lists_servers():
    # Lista de servidores de banco de dados e seus apelidos
    servidores = {'mysqld.exe': 'MySQL', 'sqlservr.exe': 'SQL Server',
                  'fbserver.exe': 'Firebird Server', 'mongodb': 'MongoDB',
                  'postgres': 'PostgreSQL'}

    # Lista de processos encontrados
    processos = []
    # Percorre todos os processos em execução
    for proc in psutil.process_iter():
        try:
            # Obtém informações do processo
            pinfo = proc.as_dict(attrs=['pid', 'name'])

            # Verifica se o nome do processo corresponde a algum dos servidores de banco de dados
            for servidor in servidores:
                if re.search(servidor, pinfo['name'], re.IGNORECASE):
                    processos.append(servidores.get(servidor))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Remove duplicatas da lista de processos encontrados
    processos = list(set(processos))

    # Transforma a lista de processos encontrados em uma string
    processos_str = " - ".join(processos)
    return processos_str

class Manger_Connect:
    def conect_db(self):
        self.conn = sqlite3.connect('venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\u.db')
        self.cursor = self.conn.cursor()
    def conect_close(self):
        try:
            self.conn.close()
        except:
            pass
    #CONECTA A DATABASE TECH_TOOLS E DEMAIS FUNÇÕES DESSE BANCO ####################################
    def contect_techtools(self):
        self.conn_tech = sqlite3.connect('venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\techtools.db')
        self.cursor_tech = self.conn_tech.cursor()


    def version_sistem_tech(self):
        try:
            self.contect_techtools()
            self.cursor_tech.execute('SELECT VERSION_SYSTEM FROM VERSION')
            version = self.cursor_tech.fetchall()
  
            for v in version:
                v = v[0]
            return v
        except Exception as e:
            print(e)
    ####################################################################################################
    def create_user(self,user,password,tipo):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO USERS (user, password, TYPE_US) VALUES (?,?,?)",(user,password,tipo))
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None
        
    def select_user(self,user):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT USER,PASSWORD,TYPE_US FROM USERS WHERE USER = '{user}'")
            resp = cursor.fetchall()
            return resp
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None
        
    def list_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT IDUSER,USER,PASSWORD,TYPE_US FROM USERS ")
            resp = cursor.fetchall()
            return resp
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None    

    def list_logins(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT ID,NOME,SENHA,EMAIL FROM MANAGER_PASS ")
            resp = cursor.fetchall()
            return resp
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None   

    def select_list_logins(self,nome):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT ID,NOME,SENHA,EMAIL FROM MANAGER_PASS WHERE NOME = '{nome}' ")
            resp = cursor.fetchall()
            return resp
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None   

    def select_list_users(self,nome):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT IDUSER,USER,PASSWORD FROM USERS WHERE USER = '{nome}' ")
            resp = cursor.fetchall()
            return resp
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None   

    def create_new_login(self,user,senha,email):
        try:
            cursor = self.conn.cursor()
            query = f"INSERT INTO MANAGER_PASS(NOME,SENHA,EMAIL) VALUES ('{user}','{senha}','{email}') "
            cursor.execute(query)
            self.conn.commit()
            return ("OK")
        except Exception as e:
            print("Erro ao executar a query:", e)
            return ("ERRO")             
                
    def alter_login(self,id,user,senha,email):
        try:
            cursor = self.conn.cursor()
            query = f"""UPDATE MANAGER_PASS SET NOME = "{user}",
                         SENHA = "{senha}", 
                         EMAIL = "{email}"
                         WHERE ID = {id}"""
            cursor.execute(query)
            self.conn.commit()
            return ("OK")
        except Exception as e:
            print("Erro ao executar a query:", e)
            return ("ERRO")          

    def alter_user(self, id, user, senha, tipo):
        try:
            cursor = self.conn.cursor()
            query = """UPDATE USERS SET USER = ?, PASSWORD = ?, TYPE_US = ? WHERE IDUSER = ?"""
            cursor.execute(query, (user, senha, tipo, id))
            self.conn.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return "ERRO"
        
    def delete_user(self, user_id):
        try:
            cursor = self.conn.cursor()
            # Execute a query SQL para deletar o usuário com o ID especificado
            query = f"DELETE FROM USERS WHERE IDUSER = ?"
            cursor.execute(query, (user_id,))
            self.conn.commit()
            print("Usuário deletado com sucesso.")
            return "OK"
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return "ERRO"
    def delete_login(self, user_id):
        try:
            cursor = self.conn.cursor()
            # Execute a query SQL para deletar o usuário com o ID especificado
            query = f"DELETE FROM MANAGER_PASS WHERE ID = ?"
            cursor.execute(query, (user_id,))
            self.conn.commit()
            print("Usuário deletado com sucesso.")
            return "OK"
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return "ERRO"
    
    def sqlite3_version(self):

        pass
 
#A classe abaixo está herdando tudo das classes QMainWindow do Pyside6 e Ui_MainWindow que é a classe que contém a tela criada no QtDesigner
class MainWindow(QMainWindow, Ui_MainWindow,Manger_Connect):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tech Tools")
        appIcon = QIcon(u"img\\TECH NEW LOGO.png")
        self.setWindowIcon(appIcon)
        self.setFixedSize(673, 493)
        #OBJETOS QUE INICIAM OCULTOS
        self.bt_new_version.setVisible(False)
        self.verificar_atualizacoes()
        self.label_conectando.setVisible(False)
        self.label_conectado.setVisible(False)
        self.label_script_copiado.setVisible(False)
        self.radioButton_login.setChecked(True)
        self.bt_mostrar_tabelas.setVisible(False)
        self.tooltip_sqlite.setVisible(False)
        self.bt_tela_bkp.setVisible(False)


        self.check_user_login()
        self.show_printers()
        self.show_instadores()


        version_sys = self.version_sistem_tech()
        self.lb_version.setText(str(f'   Versão: {version_sys}'))
        # self.lb_version.setVisible(bool(version_sys))

        chek = self.get_type_ac()
         # Chama a função para verificar o tipo de login
        if chek == 0:
            self.bt_users.setVisible(False)  
            self.bt_ncm_page.setVisible(False)
            self.radioButton_restaurar.setVisible(False )
            self.bt_processar_planilha.setVisible(False)

        # Defina o tamanho da coluna desejada
        column_index = 0  # Índice da coluna que você deseja redimensionar
        column_width = 442  # Largura desejada da coluna

        # Ajuste o tamanho da coluna
        self.tableWidget_show_tables.setColumnWidth(column_index, column_width)        
        ###########################################################################################################
        #MOSTRA A LISTA DE SERVIDORES DE BANCOS DE DADOS ATIVOS NA MÁQUINA
        # Chame a função lists_servers para obter a string que ela retorna
        lista_servidores = lists_servers()

        # Defina o texto do label com a lista de servidores
        self.label_servidores.setText(lista_servidores)

        # Defina se o label será visível ou não baseado na presença de texto na lista de servidores
        self.label_servidores.setVisible(bool(lista_servidores))

        # Crie uma instância de QFont para definir as propriedades do texto
        font = QFont()
        font.setBold(True)  # Define o texto em negrito
        # Crie uma instância de QColor para definir a cor do texto
        cor = QColor('#00ff7f')
        # Defina a cor do texto
        self.label_servidores.setStyleSheet(f'color: {cor.name()}')
        # Defina a fonte do texto
        self.label_servidores.setFont(font)
        ###########################################################################################################
        #TOGGLE BUTTON
        self.btn_tech_tools.clicked.connect(self.leftMenu)
        ##########################################################
        #INICIALIZAÇÃO DOS BOTÕES DE BANCOS DE DADOS FIREBIRD E SQLITE3
        # Configurar visibilidade inicial dos elementos
        self.bt_conectar_db_4.setVisible(False)
        self.txt_server_db_2.setVisible(False)
        self.bt_conectar_db_2.setVisible(False)
        self.txt_port_db.setVisible(False)
        self.comboBox_dataBases_db.currentIndexChanged.connect(self.select_datas)
        # Conectar o método ao botão bt_conectar_db
        # Conectar os sinais aos slots
        self.bt_conectar_db.clicked.connect(self.conect_dataBase)
        self.bt_conectar_db_2.clicked.connect(self.buscar_db)
        self.bt_conectar_db_3.clicked.connect(self.query)
        self.radioButton_user.clicked.connect(self.check_user_login)
        self.radioButton_login.clicked.connect(self.check_user_login)
        self.bt_conectar_db_4.clicked.connect(self.execut_i)
        self.bt_new_version.clicked.connect(self.teste)

        # Configurar visibilidade inicial dos elementos
        self.bt_conectar_db_4.setVisible(False)
        self.txt_server_db_2.setVisible(False)
        self.bt_conectar_db_2.setVisible(False)
        ############################BOTÕES TABELA IMPRESSORAS####################################################################

        self.table_printers.cellClicked.connect(self.select_line_table)
        self.bt_novo_printers.clicked.connect(self.new_driver_printer)
        self.bt_alterar_printers.clicked.connect(self.update_tb_printer)
        self.bt_baixar_printers.clicked.connect(self.execute_link_printer)

        ############################BOTÕES TABELA ARQUIVOS####################################################################
        self.table_arquivos.cellClicked.connect(self.select_line_instalers)
        self.bt_novo_arquivo.clicked.connect(self.new_file_instaler)
        self.bt_alter_arquivo.clicked.connect(self.update_file_instaler)
        self.bt_baixar_arquivo.clicked.connect(self.execute_link_arquivo)
        self.tableWidget_show_tables.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_show_tables.customContextMenuRequested.connect(self.showContextMenu)

        #########################SCRIPTS########################################################################
        # Crie um temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_label)
        
        self.load_scripts()
        self.comboBox_Scripts.currentIndexChanged.connect(self.select_combo_script)
        self.bt_new_scripts.clicked.connect(self.new_Script_combo)
        self.bt_alterar_script.clicked.connect(self.update_script_combo)
        self.bt_excluirScript.clicked.connect(self.delete_script_confirmation)
        self.bt_copiarScripts.clicked.connect(self.copy_script_combo)
        self.bt_enviar_script.clicked.connect(self.copy_send_Script)
        # Páginas do Sistema
        self.bt_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.bt_data_base.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_Data_base))
        self.bt_printers.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_printers))
        self.bt_instaladores.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_instaladores))
        self.bt_scripts.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_scripts))
        self.bt_sobre.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_Sobre))
        self.bt_termos.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_terms))
        self.bt_users.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_users))
        self.bt_mostrar_tabelas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_show_tables))
        self.bt_ncm_page.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_ncm))
        self.bt_executaveis.clicked.connect(lambda:self.pages.setCurrentWidget(self.pg_executaveis))
        self.bt_tela_bkp.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_bkp_rest))
        self.bt_processar_planilha.clicked.connect(self.mostrar_janela_processamento_csv)
        ##################################################################################################

        self.bt_novo_user_login.clicked.connect(self.create_new_login_user)
        self.bt_alterar_user_login.clicked.connect(self.alter_login_user)
        self.bt_excluir_user_login.clicked.connect(self.delete_user_login)
        self.tableWidget_user_login.clicked.connect(self.select_line_user_login)

        ##############PAGINA DE NCM########################################################################################
        self.label_siscomex.setVisible(False)
        self.radioButton_list_ncm.setChecked(True)
        self.check_tb_ncm()
        self.radioButton_list_ncm.clicked.connect(self.check_tb_ncm)
        self.radioButton_ncm_dataBases.clicked.connect(self.check_tb_ncm)
        self.bt_salvar_ncm.clicked.connect(self.save_data_ncm)
        self.txt_ncm.textChanged.connect(self.filtrar_ncm)
        self.bt_buscarncm_database.clicked.connect(self.buscar_ncm_inDataBases)
        self.carregar_dados_ncm()

        self.bt_executar_exe.clicked.connect(self.executar_programa)
        ###################PÁGINA BACKUP DATA BASES #######################################################################
        self.radioButton_backup.setChecked(True)
        self.lb_local_arquivo.setVisible(False)
        self.txt_path_bkp_rest.setVisible(False)
        self.pushButton_buscar_backup.setVisible(False)
        self.bt_Restaurao.setVisible(False)
        self.radioButton_backup.clicked.connect(self.select_bkp_rest)
        self.radioButton_restaurar.clicked.connect(self.select_bkp_rest)
        self.bt_Backup.clicked.connect(self.backup_database)
        self.pushButton_buscar_backup.clicked.connect(self.buscar_backup)
        self.bt_Restaurao.clicked.connect(self.restaure_database)
    def teste(self):
        print("Botão clicado")
    def verificar_atualizacoes(self):
        # URL da API do GitHub para acessar os lançamentos do repositório
        url = "https://api.github.com/repos/EduardoFerreira22/Tech_Tools/releases"
        token = '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'

        headers = {'Authorization': f'token {token}'}

        try:
            # Faz uma solicitação HTTP para a API do GitHub
            r = requests.get(url, headers=headers)

            # Verifica se a solicitação foi bem-sucedida
            if r.status_code != 200:
                print("Erro ao acessar a API do GitHub.")
                return

            # Analisa a resposta em formato JSON
            releases = r.json()

            # Verifica se há lançamentos disponíveis
            if not releases:
                print("Sem atualizações disponíveis.")
                return


            # Obtém a versão mais recente do programa e a URL do arquivo ZIP
            ultima_versao = releases[0]["tag_name"]
            print(ultima_versao)

            # Use o link direto para o arquivo ZIP da versão específica
            url_download = releases[0]["zipball_url"]
            response = requests.get(url_download, stream=True)


            # Lê a versão atual do programa do arquivo "version.txt"
            path_v = os.path.join("..","venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\version.txt")
            arquivo_version = "0.0"
            if os.path.exists(path_v):
                with open(path_v, 'r') as file_version:
                    version = file_version.readline()
                    if version.startswith("Version_app:"):
                        arquivo_version = version[len("Version_app: "):].strip()

            # Compara as versões
            if ultima_versao > arquivo_version:
                self.bt_new_version.setVisible(True)
                

        except Exception as e:
            print(f"Erro: {e}")
    
    #FUNÇÃO PARA ESCONDER A BARRA DE MENU LATERAL
    def leftMenu(self):
        width = self.left_frame.width()

        if width == 0:
            newWidth = 120
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.left_frame, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def msg_popup(self,resp,msg1,msg2,**kwargs):
        msg1 = msg1
        msg2 = msg2
        if resp == 'OK':
            self.label_conectando.setVisible(False)
            self.label_conectado.setVisible(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sucesso!")
            msg.setText(f"{msg1}")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"{msg2}")
            msg.exec()
    #####################################################################################################
    #SELECIONA A OPÇÃO DE CONEXÃO DE BANCO DE DADOS NO COMBOBOX DA PÁGINA CONEXÕES
    def select_datas(self):

        selected_data = self.comboBox_dataBases_db.currentText()

        # Verifica se a opção selecionada é 'SQLite3'
        if selected_data == 'FireBird':
            # Se for 'SQLite3', torna o botão visível
            self.bt_conectar_db_4.setVisible(True)
            self.output_query.appendPlainText("IBExpert selecionado com sucesso!")
            self.txt_port_db.setVisible(False)
        else:
            # Caso contrário, torna o botão invisível
            self.bt_conectar_db_4.setVisible(False)

        # Verifica se a opção selecionada é 'Firebird'
        if selected_data == 'SQLite3':
            # Se for 'Firebird', torna os elementos visíveis
            self.output_query.appendPlainText("Opção SQLite selecionado com sucesso!")
            self.tooltip_sqlite.setVisible(True)
            self.txt_server_db_2.clear()
            self.txt_server_db_2.setVisible(True)
            self.bt_conectar_db_2.setVisible(True)
            self.txt_server_db.clear()
            self.txt_dataBase_db.clear()
            self.txt_user_db.clear()
            self.txt_pass_db.clear()
            self.txt_port_db.setVisible(False)
        else:
            # Caso contrário, torna os elementos invisíveis
            self.txt_server_db_2.setVisible(False)
            self.bt_conectar_db_2.setVisible(False)

        if selected_data == 'PostgreSQL':
            self.txt_port_db.setVisible(True)
        elif selected_data == 'MySQL':
            self.txt_port_db.setVisible(True)
        elif selected_data == 'SQL Server':
            self.txt_port_db.setVisible(False)

    
    def check_cache(self):
        path = "venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\users.txt"
        if os.path.exists(path):
            with open(path, 'r') as r:
                line = r.readline()
                if line.startswith("User:"):
                    user_cache = line[len("User: "):].strip()
                    return user_cache
        else:
            print('não foi possível retornar o cache')
            pass    
    
    def get_type_ac(self):
        check = self.check_cache()
        conn = Manger_Connect()
        conn.conect_db()
        query_ac = "SELECT USER,TYPE_US FROM USERS WHERE USER = ?"
        conn.cursor.execute(query_ac, (check,))
        res = conn.cursor.fetchall()
        for x in res:
                tipo_acess = x[1]
                return tipo_acess
    
    ####################################################################################################################
    # FAZ A CONEXÃO COM O BANCO DE DADOS SQL SERVER
    def conectar_ao_sql_server(self):
        server = self.txt_server_db.text()
        database = self.txt_dataBase_db.text()
        user = self.txt_user_db.text()
        password = self.txt_pass_db.text()
        if server == '' and database == '' and user == '' and password == '':
            self.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")
            self.output_query.appendPlainText(f"Erro! dados incompletos.")
        else:
            msg1 = "Conectado com Sucesso!"
            msg2 = f"Não foi possível se conectar ao banco de dados {database}"

            # Instancie a classe Conections_SQLServer com os argumentos necessários
            self.conn1 = conect.Conections_SQLServer()
            resp = self.conn1.conect_sqlserver(server, database, user, password)
            
            if resp == 'OK':
                self.output_query.appendPlainText(f"{msg1}")
            elif resp == 'ERRO':
                self.output_query.appendPlainText(f"Erro: {msg2}")

            self.msg_popup(resp,msg1,msg2)
            
            self.bt_tela_bkp.setVisible(True)

    #Conectando #############################################################################    
    def conectar_ao_MySQL(self):
            server = self.txt_server_db.text()
            database = self.txt_dataBase_db.text()
            user = self.txt_user_db.text()
            password = self.txt_pass_db.text()
            port = self.txt_port_db.text()
            if server == '' and database == '' and user == '':
                self.output_query.appendPlainText(f"Erro! dados incompletos.")
                self.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")
            
            else:
                msg1 = "Conectado com Sucesso!"
                msg2 = f"Não foi possível se conectar ao banco de dados {database}"
                
                if port == '' or port == None:
                    port = '3306'

                self.conn2 = conect.Conections_MySQL()
                resp = self.conn2.MYSQL(server, database, user, password, port=port)

                if resp == 'OK':
                    self.output_query.appendPlainText(f"{msg1}")
                elif resp == 'ERRO':
                    self.output_query.appendPlainText(f"Erro: {msg2}")                
                self.msg_popup(resp,msg1,msg2)

    def conectar_ao_PostgreSQL(self):
        server = self.txt_server_db.text()
        database = self.txt_dataBase_db.text()
        user = self.txt_user_db.text()
        password = self.txt_pass_db.text()
        port = self.txt_port_db.text()


        if server == '' and database == '' and user == '' and password == '':
            self.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")
            self.output_query.appendPlainText(f"Erro! dados incompletos.")
        else:
            msg1 = "Conectado com Sucesso!"
            msg2 = f"Não foi possível se conectar ao banco de dados {database}"
            if port == '' or port == None:
                port = '5432'
            # Instancie a classe Conections_SQLServer com os argumentos necessários
            self.conn4 = conect.Conections_PostgreSQL()
            resp = self.conn4.postgresql_conect(server, database, user, password, port)
            
            if resp == 'OK':
                self.output_query.appendPlainText(f"{msg1}")
            elif resp == 'ERRO':
                self.output_query.appendPlainText(f"Erro: {msg2}")

            self.msg_popup(resp,msg1,msg2)
            
            # self.bt_tela_bkp.setVisible(True)

    def buscar_db(self):
        # Abre um diálogo de seleção de arquivo
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Banco de Dados SQLite (*.db *.sqlite *.sqlite3);;Todos os Arquivos (*)")

        if file_dialog.exec_():
            # Obtém o caminho do arquivo selecionado
            selected_file = file_dialog.selectedFiles()[0]

            # Define o caminho no QLineEdit
            self.txt_server_db_2.setText(selected_file)
            self.txt_server_db_2.setVisible(True)  

    def buscar_sqlite3(self):
        self.conn3 = conect.Conections_SQLite3()
        caminho = self.txt_server_db_2.text()
        
        if caminho == '':
            self.output_query.appendPlainText(f"Erro! dados incompletos.")
            self.show_error_popup("Erro!","Não foi possível identificar o caminho para o banco de dados\nConexão não realizada.")
        else:
            print(f"Caminho do Banco de Dados: {caminho}")  # Adicione esta linha para depurar
            resp = self.conn3.conectar_sqlite3_db(caminho)
            msg1 = "Conectado com Sucesso!"
            msg2 = f"Não foi possível se conectar ao banco de dados"

            if resp == 'OK':
                self.cache_path = 'venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\cache.txt'
                with open(self.cache_path, 'w') as cache_file:
                    cache_file.write(caminho)
                self.label_conectando.setVisible(False)
                self.label_conectado.setVisible(True)
                self.msg_popup(resp, msg1, msg2)
                if resp == 'OK':
                    self.output_query.appendPlainText(f"{msg1}")
                elif resp == 'ERRO':
                    self.output_query.appendPlainText(f"Erro: {msg2}")   
            return self.conn3  # Retorna o objeto de conexão em vez da string 'OK'

   
    def conect_dataBase(self):
        selected_data = self.comboBox_dataBases_db.currentText()
        if selected_data == 'SQL Server':
            self.label_conectando.setVisible(True)
            self.conectar_ao_sql_server()
            self.bt_mostrar_tabelas.setVisible(True)
            databases = self.list_DataBases()
            self.combo_list_database.clear()
            self.combo_list_database.addItems(databases)
            tables = self.tables_SqlServer()
            self.showTables_in_Table(tables)
        elif selected_data == 'MySQL':
            self.label_conectando.setVisible(True)
            self.conectar_ao_MySQL()
            self.bt_mostrar_tabelas.setVisible(True)
            tables = self.tables_MySQL()
            self.showTables_in_Table(tables)
        elif selected_data == 'SQLite3':
            self.label_conectando.setVisible(True)
            conn3 = self.buscar_sqlite3()  # Obtém o objeto de conexão
            tables = self.tables_SQLite3()  # Obtém as tabelas do SQLite3
            self.showTables_in_Table(tables)
            self.bt_mostrar_tabelas.setVisible(True)
        elif selected_data == 'PostgreSQL':
            self.label_conectando.setVisible(True)
            self.conectar_ao_PostgreSQL()
            self.bt_mostrar_tabelas.setVisible(True)
            tables = self.tables_PostgreSQL()
            self.showTables_in_Table(tables)

    def list_DataBases(self):
        try:
            self.conn1.cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
            databases = [database[0] for database in self.conn1.cursor.fetchall()]
            print(databases)
            return databases
        except pyodbc.Error as err:
            print("Erro ao conectar ao SQL Server:", err)
            return []

    def select_bkp_rest(self):

        if self.radioButton_backup.isChecked():
            self.label_7.setVisible(True)
            self.combo_list_database.setVisible(True)
            self.bt_Backup.setVisible(True)
            self.txt_path_bkp_rest.setVisible(False)
            self.lb_local_arquivo.setVisible(False)
            self.pushButton_buscar_backup.setVisible(False)
            self.bt_Restaurao.setVisible(False)
        elif self.radioButton_restaurar.isChecked():
            self.label_7.setVisible(False)
            self.combo_list_database.setVisible(False)
            self.bt_Backup.setVisible(False)
            self.lb_local_arquivo.setVisible(True)
            self.txt_path_bkp_rest.setVisible(True)
            self.pushButton_buscar_backup.setVisible(True)
            self.bt_Restaurao.setVisible(True)
    # BACKUPS DE DATABASES SQL SERVER
    def backup_database(self):
        tipo_banco = 'sqlserver'
        server = self.txt_server_db.text()
        nome_banco = self.combo_list_database.currentText()
        user = self.txt_user_db.text()
        password = self.txt_pass_db.text()

        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix(".bak")
        file_dialog.setNameFilter("Arquivos de backup (*.bak)")
        file_dialog.setOption(QFileDialog.DontConfirmOverwrite, False)
        directory, _ = file_dialog.getSaveFileName(self, "Salvar backup do banco de dados", f"{nome_banco}.bak", "Arquivos de backup (*.bak)")

        if directory:  # directory contém o caminho do arquivo selecionado
            try:
                if tipo_banco.lower() == 'sqlserver':
                    comando_backup = f'sqlcmd -S {server} -d {nome_banco} -U {user} -P {password} -Q "BACKUP DATABASE {nome_banco} TO DISK=\'{directory}\'"'
                elif tipo_banco.lower() == 'mysql':
                    comando_backup = f'mysqldump -u {user} -p{password} {nome_banco} > {directory}'
                else:
                    self.output_log_bkp_rest.appendPlainText("Tipo de banco de dados inválido")
                    print("Tipo de banco de dados inválido.")
                    return

                try:
                    # Captura a saída do subprocesso e exibe no output_log_bkp_rest
                    output = subprocess.run(comando_backup, shell=True, check=True, capture_output=True, text=True)
                    self.output_log_bkp_rest.appendPlainText(output.stdout)
                    self.output_log_bkp_rest.appendPlainText(f"Arquivo selecionado para backup: {directory}")
                    self.output_log_bkp_rest.appendPlainText("Backup realizado com sucesso!")
                    
                except subprocess.CalledProcessError as e:
                    self.output_log_bkp_rest.appendPlainText(f"Erro ao realizar o backup: {e.stderr}")
                except Exception as e:
                    self.output_log_bkp_rest.appendPlainText(f"Erro inesperado: {e}")
                    print(f"Erro inesperado: {e}")
            except Exception as e:
                pass
            print(f"Arquivo selecionado para backup: {directory}")

    # BUSCA O CAMINHO PARA 
    def buscar_backup(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setNameFilter("Arquivos de backup (*.bak)")
        file_dialog.setOption(QFileDialog.DontConfirmOverwrite, False)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setWindowTitle("Selecionar arquivo de backup")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()[0]

            self.txt_path_bkp_rest.clear()
            self.txt_path_bkp_rest.setText(selected_files)

    def restaure_database(self):
        backup_file = self.txt_path_bkp_rest.text()
        tipo_banco = 'sqlserver'  # Defina o tipo de banco de dados conforme necessário
        server = self.txt_server_db.text()
        user = self.txt_user_db.text()
        password = self.txt_pass_db.text()
        self.output_log_bkp_rest.appendPlainText(f"Iniciando...")
        self.output_log_bkp_rest.appendPlainText(f"Caminho Data Base selecionado:\n{backup_file}")
        if tipo_banco.lower() == 'sqlserver':
            # Extrair o nome do arquivo sem a extensão
            nome_banco = os.path.splitext(os.path.basename(backup_file))[0]
            self.output_log_bkp_rest.appendPlainText(f"Data Base: {nome_banco}")
            print(nome_banco)
        else:
            nome_banco = None

        try:
            if tipo_banco.lower() == 'sqlserver':
                comando_restauracao = f'sqlcmd -S {server} -d master -U {user} -P {password} -Q "RESTORE DATABASE {nome_banco} FROM DISK=\'{backup_file}\'"'
            elif tipo_banco.lower() == 'mysql':
                comando_restauracao = f'mysql -u {user} -p{password} {nome_banco} < {backup_file}'
            else:
                self.output_log_bkp_rest.appendPlainText("Tipo de banco de dados inválido.")
                print("Tipo de banco de dados inválido.")
                return

            try:
                subprocess.run(comando_restauracao, shell=True, check=True)
                print("Restauração realizada com sucesso!")

                # Exibir os dados de saída no output de logs
                output_log = f"Restauração realizada com sucesso!\n"
                output_log += subprocess.check_output(comando_restauracao, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
                self.output_log_bkp_rest.appendPlainText(output_log)
            except subprocess.CalledProcessError as e:
                print(f"Erro ao realizar a restauração: {e}")
            except Exception as e:
                self.output_log_bkp_rest.appendPlainText(f"Erro inesperado: {e}")

        except Exception as e:
            self.output_log_bkp_rest.appendPlainText(f"Erro ao restaurar o banco de dados: {e}")

    def open_secondary_window(self):
        self.secondary_window = SQLWindown()  # Instanciando a tela secundária
        self.secondary_window.setupUi(self.secondary_window)  # Configurando a interface da tela secundária
        self.secondary_window.show()  # Exibindo a tela secundária

    def buscar_cache(self):
        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'r') as file:
                cache = file.readline().strip()  # Remover espaços em branco e quebras de linha
                if cache:
                    self.txt_server_db_2.setText(cache)
                    return cache
        else:
            print("Arquivo de cache não encontrado.")

    def query(self):
        error = Erros()
        query_value = self.plainTextEdit.toPlainText()
        selected_data = self.comboBox_dataBases_db.currentText()
        
        try:
            if selected_data == 'SQL Server':
                self.execute_sql_server_query(query_value)
            elif selected_data == 'MySQL':
                self.execute_mysql_query(query_value)
            elif selected_data == 'SQLite3':
                self.execute_sqlite_query(query_value)
            elif selected_data == 'PostgreSQL':
                self.execute_PostgreSQL_query(query_value)
            else:
                self.output_query.appendPlainText("Banco de dados selecionado não suportado.")
                print("Banco de dados selecionado não suportado.")
        except Exception as e:
            error.show_error_popup(str(e))

    def execute_sql_server_query(self, query):
        try:
            self.conn1.cursor.execute(query)
            if query.strip().upper().startswith('SELECT'):
                resp = self.conn1.cursor.fetchall()
                column_names = [column[0] for column in self.conn1.cursor.description]
                self.display_query_results(column_names, resp)
            else:
                self.output_query.appendPlainText("Comando SQL Server executado com sucesso.")
        except Exception as e:
            self.output_query.appendPlainText("Erro ao executar o comando SQL Server: " + str(e))

    def execute_mysql_query(self, query):
        try:
            self.conn2.cursor.execute(query)
            if query.strip().upper().startswith('SELECT'):
                resp = self.conn2.cursor.fetchall()
                column_names = self.conn2.cursor.column_names
                self.display_query_results(column_names, resp)
            else:
                self.output_query.appendPlainText("Comando MySQL executado com sucesso.")
        except Exception as e:
            self.output_query.appendPlainText("Erro ao executar o comando MySQL: " + str(e))

    def execute_sqlite_query(self, query):
        try:
            cache = self.buscar_cache()
            if cache:
                self.conn3.conectar_sqlite3_db(cache)
                self.conn3.cursor.execute(query)
                if query.strip().upper().startswith('SELECT'):
                    res = self.conn3.cursor.fetchall()
                    column_names = [description[0] for description in self.conn3.cursor.description]
                    self.display_query_results(column_names, res)
                else:
                    self.output_query.appendPlainText("Comando SQLite executado com sucesso.")
            else:
                self.output_query.appendPlainText("Nenhum caminho de banco de dados SQLite encontrado no arquivo de cache.")
        except Exception as e:
            self.output_query.appendPlainText("Erro ao executar o comando SQLite: " + str(e))

    def execute_PostgreSQL_query(self, query):
        try:
            # Executar a consulta
            self.conn4.cursor.execute(query)
            # Verificar se a consulta é uma consulta SELECT
            if query.strip().upper().startswith('SELECT'):
                # Recuperar os resultados da consulta
                resp = self.conn4.cursor.fetchall()
                # Recuperar os nomes das colunas
                column_names = [column.name for column in self.conn4.cursor.description]
                # Exibir os resultados da consulta
                self.display_query_results(column_names, resp)
            else:
                self.output_query.appendPlainText("Comando PostgreSQL executado com sucesso.")

            # Fechar o self.conn4.cursor
            self.conn4.cursor.close()

        except Exception as e:
            self.output_query.appendPlainText("Erro ao executar o comando PostgreSQL: " + str(e))

    def display_query_results(self, column_names, data):
        self.open_secondary_window() 
        if hasattr(self, 'secondary_window') and isinstance(self.secondary_window, SQLWindown):
            self.secondary_window.update_table_data(column_names, data)
        else:
            print("Tela secundária não foi inicializada corretamente.")

            # Mostrar a saída da consulta no QPlainTextEdit
            self.output_query.appendPlainText("Resultado da consulta:")
            for row in data:
                self.output_query.appendPlainText(str(row))

    def tables_SqlServer(self):
        data = self.txt_dataBase_db.text()
        try:
            self.conn1.cursor.execute(f"""SELECT TABLE_NAME
                                            FROM INFORMATION_SCHEMA.TABLES
                                            WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = '{data}'""")
            resp = self.conn1.cursor.fetchall()
            return resp
        except Exception as e:
            print(e)

    def tables_MySQL(self):
        data = self.txt_dataBase_db.text()
        try:
            self.conn2.cursor.execute(f"""SELECT TABLE_NAME
                                            FROM INFORMATION_SCHEMA.TABLES
                                            WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = '{data}'""")
            resp = self.conn2.cursor.fetchall()
            return resp
        except Exception as e:
            print(e)
        
    def tables_PostgreSQL(self):
        try:
            self.conn4.cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
            """)
            resp = self.conn4.cursor.fetchall()
            return resp
        except psycopg2.Error as e:
            print(f"Erro ao buscar tabelas: {e}")
            return []

    def tables_SQLite3(self):
        try:
            self.conn3.cursor.execute("""SELECT name
                                        FROM sqlite_master
                                        WHERE type='table'""")
            resp = self.conn3.cursor.fetchall()
            return resp
        except Exception as e:
            print(e)

    def showTables_in_Table(self, tables):
        # Limpa qualquer conteúdo existente na tabela widget
        self.tableWidget_show_tables.clearContents()
        self.tableWidget_show_tables.setRowCount(0)

        if tables is not None:  # Verifica se a lista de tabelas não é None
            # Define o número de linhas na tabela widget baseado no número de tabelas
            self.tableWidget_show_tables.setRowCount(len(tables))

            # Insere os dados das tabelas na tabela widget
            for row_idx, table_name in enumerate(tables):
                item = QTableWidgetItem(table_name[0])
                self.tableWidget_show_tables.setItem(row_idx, 0, item)
        else:
            print("Nenhuma tabela encontrada.")
            # Adicione aqui qualquer ação que você deseja executar caso nenhuma tabela seja encontrada


    def execut_i(self):
        path = 'resource\\ibexpert.exe'
        subprocess.run(path)

    def mostrar_janela_processamento_csv(self):
        self.janela_processamento_csv = Processing_CSV()
        self.janela_processamento_csv.show()

    def executar_programa(self):
        # Obtenha o nome do executável selecionado no combobox
        nome_executavel = self.comboBox_executaveis.currentText()
        
        # Mapeie o nome do executável selecionado para o caminho completo do arquivo executável
        executaveis = {
            "Advanced_IP_Scanner": "resource\\Advanced_IP_Scanner.exe",
            "AnyDesk": "resource\\AnyDesk.exe",
            "Ativador Mágico": "resource\\ATIVADOR MAGICO.cmd",
            "CrystalDiskInfo": "resource\\CrystalDiskInfo.exe",
            "Drives de Rede 3DP": "resource\\3DP.exe",
            "Rufus": "resource\\Rufus.exe",
            "WinToHDD_Free": "resource\\WinToHDD_Free.exe"
        }
        
        # Verifique se o nome do executável está mapeado
        if nome_executavel in executaveis:
            # Obtenha o caminho do executável correspondente
            caminho_executavel = executaveis[nome_executavel]
            
            # Execute o executável
            subprocess.run([caminho_executavel])
        else:
            self.show_error_popup("Erro!","Executável não encontrado.")

    def showContextMenu(self, position):
        # Obter posição da célula clicada
        index = self.tableWidget_show_tables.indexAt(position)
        if index.isValid():
            row = index.row()
            column = index.column()
            # Obter texto da célula clicada
            cell_text = self.tableWidget_show_tables.item(row, column).text()
            print(cell_text)
            # Criar menu de contexto
            menu = QMenu(self)
            # Criar ação para a opção "Mostrar"
            show_action = menu.addAction("Mostrar")
            # Conectar a ação ao slot que executa a consulta com base no texto da célula clicada
            show_action.triggered.connect(lambda  text=cell_text: self.query_table_list(cell_text))
            # Exibir menu na posição do clique
            menu.exec(self.tableWidget_show_tables.viewport().mapToGlobal(position))

    def query_table_list(self,table):
        error = Erros()

        selected_data = self.comboBox_dataBases_db.currentText()
        if selected_data == 'SQL Server':
            try:
                print(table)
                query_value = f"""SELECT * FROM [{table}]"""
                self.conn1.cursor.execute(query_value)
                resp = self.conn1.cursor.fetchall()
                # Recupera os nomes das colunas
                column_names = [column[0] for column in self.conn1.cursor.description]
                self.open_secondary_window() 
                if hasattr(self, 'secondary_window') and isinstance(self.secondary_window, SQLWindown):
                    self.secondary_window.update_table_data(column_names,resp)  
                else:
                    print("Tela secundária não foi inicializada corretamente.")
            except Exception as e:
                error.show_error_popup(str(e)) 
                print(e) 

        elif selected_data == 'MySQL':
            try:
                query_value = f"""SELECT * FROM {table};"""
                self.conn2.cursor.execute(query_value)
                resp = self.conn2.cursor.fetchall()
                # Recupera os nomes das colunas
                column_names = self.conn2.cursor.column_names
                self.open_secondary_window() 
                if hasattr(self, 'secondary_window') and isinstance(self.secondary_window, SQLWindown):
                    self.secondary_window.update_table_data(column_names,resp)  
                else:
                    print("Tela secundária não foi inicializada corretamente.")
            except Exception as e:
                error.show_error_popup(str(e))
                print(e)

        elif selected_data == 'PostgreSQL':
            try:
                query_value = f"""SELECT * FROM {table};"""
                self.conn4.cursor.execute(query_value)
                resp = self.conn4.cursor.fetchall()

                # Recupera os nomes das colunas do cursor.description
                column_names = [desc[0] for desc in self.conn4.cursor.description]

                self.open_secondary_window() 
                if hasattr(self, 'secondary_window') and isinstance(self.secondary_window, SQLWindown):
                    self.secondary_window.update_table_data(column_names, resp)  
                else:
                    print("Tela secundária não foi inicializada corretamente.")
            except Exception as e:
                error.show_error_popup(str(e))
                print(e)

        elif selected_data == 'SQLite3':
            cache = self.buscar_cache()
            try:
                if cache:
                    query_value = f"SELECT * FROM {table};"
                    self.conn3.conectar_sqlite3_db(cache)
                    self.conn3.cursor.execute(query_value)
                    res = self.conn3.cursor.fetchall()
                    # Recupera os nomes das colunas
                    column_names = [description[0] for description in self.conn3.cursor.description]
                    print(res)
                    self.open_secondary_window() 
                    if hasattr(self, 'secondary_window') and isinstance(self.secondary_window, SQLWindown):
                        self.secondary_window.update_table_data(column_names, res)
                    else:
                        print("Tela secundária não foi inicializada corretamente.")
                else:
                    print("Nenhum caminho de banco de dados SQLite encontrado no arquivo de cache.")
            except Exception as e:
                resp = e

    
    def mostrarItemSelecionado(self):
        # Implemente a lógica para mostrar o item selecionado
        selected_item = self.tableWidget_show_tables.selectedItems()
        # Aqui você pode trabalhar com o item selecionado e exibir conforme necessário
    #######################EXECUTA QUERYS RELACIONADAS AS TABELAS DRIVERS IMPRESSORAS E INSTALADORES###############################################
    def show_printers(self):
        conn = SQLite_Data()
        conn.conect_db()
        printers = conn.select_printers()
        if printers:
            self.table_printers.setRowCount(len(printers))
            self.table_printers.setColumnCount(1)  # Uma coluna para a descrição das impressoras
            for i, printer in enumerate(printers):
                item = QTableWidgetItem(printer[0])
                self.table_printers.setItem(i, 0, item)
        else:
            print("Nenhuma impressora encontrada ou erro ao recuperar dados.")

    def select_line_table(self, row):
        conn = SQLite_Data()
        item = self.table_printers.item(row, 0).text()
        print("Item:", item)
        conn.conect_db()
        lista = conn.select_printer_tables(item)

        # Verifica se a lista não é None
        if lista is not None:
            for l in lista:
                id = l[0]
                desc = l[1]
                link = l[2]
                print("Descrição:", desc)
                print("Link:", link)

                # Verifique se os QLineEdit estão corretamente configurados
                print("txt_nome_printers:", self.txt_nome_printers)
                print("txt_link_printers:", self.txt_link_printers)

                self.txt_id_printer.setText(str(id))
                self.txt_nome_printers.setText(desc)
                self.txt_link_printers.setText(link)
        else:
            # Se a lista for None, você pode definir os QLineEdit como vazios
            self.txt_id_printer.setText("")
            self.txt_nome_printers.setText("")
            self.txt_link_printers.setText("")

    def new_driver_printer(self):
        desc = self.txt_nome_printers.text()
        link = self.txt_link_printers.text()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.new_printer(desc,link)
        msg1 = "Novo Driver Cadastrado"
        msg2 = "Não foi possível registrar os dados"
        self.show_printers()
        self.msg_popup(resp,msg1,msg2)

    def update_tb_printer(self):
        id_p = self.txt_id_printer.text()
        desc = self.txt_nome_printers.text()
        link = self.txt_link_printers.text()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.update_printers(desc,link,id_p)
        msg1 = "Atualizado com Sucesso!"
        msg2 = "Não foi possível atualizar os dados"
        self.show_printers()
        self.msg_popup(resp,msg1,msg2)

    def execute_link_printer(self):
        link = self.txt_link_printers.text()
        # Abre o link no navegador padrão
        QDesktopServices.openUrl(QUrl(link))

    def show_instadores(self):
        conn = SQLite_Data()
        conn.conect_db()
        instalers = conn.select_instalers()
        if instalers:
            self.table_arquivos.setRowCount(len(instalers))
            self.table_arquivos.setColumnCount(1)  # Uma coluna para a descrição das impressoras
            for i, printer in enumerate(instalers):
                item = QTableWidgetItem(printer[0])
                self.table_arquivos.setItem(i, 0, item)
        else:
            print("Nenhuma impressora encontrada ou erro ao recuperar dados.")

    def select_line_instalers(self, row):
        conn = SQLite_Data()
        item = self.table_arquivos.item(row, 0).text()
        print("Item:", item)
        conn.conect_db()
        lista = conn.select_instalers_tables(item)

        # Verifica se a lista não é None
        if lista is not None:
            for l in lista:
                id = l[0]
                desc = l[1]
                link = l[2]
                print("Descrição:", desc)
                print("Link:", link)

                # Verifique se os QLineEdit estão corretamente configurados
                print("txt_nome:", self.txt_nome_arquivo)
                print("txt_link:", self.txt_link_arquivo)

                self.txt_id_instaler.setText(str(id))
                self.txt_nome_arquivo.setText(desc)
                self.txt_link_arquivo.setText(link)
        else:
            # Se a lista for None, você pode definir os QLineEdit como vazios
                self.txt_id_instaler.setText("")
                self.txt_nome_arquivo.setText("")
                self.txt_link_arquivo.setText("")
        
    def new_file_instaler(self):
        desc = self.txt_nome_arquivo.text()
        link = self.txt_link_arquivo.text()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.new_istaler(desc,link)
        msg1 = "Novo arquivo de instalação Cadastrado"
        msg2 = "Não foi possível registrar os dados"
        self.show_instadores()
        self.msg_popup(resp,msg1,msg2)

    def update_file_instaler(self):
        id_p = self.txt_id_instaler.text()
        desc = self.txt_nome_arquivo.text()
        link = self.txt_link_arquivo.text()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.update_instaler(desc,link,id_p)
        msg1 = "Atualizado com Sucesso!"
        msg2 = "Não foi possível atualizar os dados"
        self.show_instadores()
        self.msg_popup(resp,msg1,msg2)

    def execute_link_arquivo(self):
        link = self.txt_link_arquivo.text()
        # Abre o link no navegador padrão
        QDesktopServices.openUrl(QUrl(link))    
    
    ###################EXECUTA FUNÇÕES RELACIONADAS A TELA SCRIPTS ##################################################################################
    def load_scripts(self):
        conn = SQLite_Data()
        conn.conect_db()
        res = conn.select_scripts()
        # Limpa o combobox antes de adicionar os novos itens
        self.comboBox_Scripts.clear()
        # Adiciona os itens retornados da consulta ao combobox
        for script in res:
            # Verifica se o item é uma tupla e pega o primeiro elemento
            if isinstance(script, tuple):
                script = script[0]
            self.comboBox_Scripts.addItem(script)

    def select_combo_script(self,index):
        # Obtém o item selecionado pelo índice do combobox
        selected_item = self.comboBox_Scripts.itemText(index)
        print(selected_item)
        conn = SQLite_Data()
        conn.conect_db()
        res = conn.combo_script_itens(selected_item)
        if res is not None:
            for s in res:
                id = s[0]
                desc = s[1]
                scr = s[2]

                self.txt_id_script.setText(str(id))
                self.txt_descript_script.setText(str(desc))
                self.txt_Scripts.setPlainText(str(scr))
        else:
            pass

    def new_Script_combo(self):
        desc = self.txt_descript_script.text()
        script = self.txt_Scripts.toPlainText()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.new_istaler(str(desc),str(script))
        msg1 = f"Novo script Cadastrado com sucesso!\n{desc}"
        msg2 = "Não foi possível registrar os dados"
        self.load_scripts()
        self.msg_popup(resp,msg1,msg2)       

    def update_script_combo(self):
        id = self.txt_id_script.text()
        desc = self.txt_descript_script.text()
        script = self.txt_Scripts.toPlainText()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.update_script(str(desc),str(script),id)
        msg1 = f"Script atualizado com sucesso!"
        msg2 = "Não foi possível atualizar os dados"
        self.load_scripts()
        self.msg_popup(resp,msg1,msg2) 
        self.txt_id_script.clear()
        self.txt_descript_script.clear()
        self.txt_Scripts.clear()   

    def delete_script_combo(self):
        id = self.txt_id_script.text()
        conn = SQLite_Data()
        conn.conect_db()
        resp = conn.delete_script(id)
        msg1 = f"Script deletado com sucesso!"
        msg2 = "Não foi possível deletar os dados selecionados"
        self.load_scripts()
        self.msg_popup(resp,msg1,msg2)  

    def delete_script_confirmation(self):
        # Exibir uma caixa de diálogo de confirmação
        reply = QMessageBox.question(self, 'Confirmar Exclusão', 
            "Tem certeza de que deseja excluir o script selecionado?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Se o usuário clicou em Sim, chame a função para excluir o script
            self.delete_script_combo()
        else:
            # Se o usuário clicou em Não, não faça nada
            pass
    
    def copy_script_combo(self):
        # Obter o texto do QPlainTextEdit
        script = self.txt_Scripts.toPlainText()
        # Copiar o texto para a área de transferência
        QApplication.clipboard().setText(script)
        self.label_script_copiado.setVisible(True)

        # Inicie o temporizador para ocultar o QLabel após 5 segundos
        self.timer.start(5000)  # 5000 milissegundos = 5 segundos

    def hide_label(self):
        # Oculte o QLabel
        self.label_script_copiado.setVisible(False)

    # MOSTRA OS DADOS NA TABELA DE USUÁRIOS OU DE LOGIN DE ACORDO COM O CHECK QUE ESTÁ SELECIONADO
    def check_user_login(self):
        conn = Manger_Connect()

        if self.radioButton_login.isChecked():
            self.comboBox_tipo.setVisible(False)
            self.txt_email_usre.setVisible(True)
            conn.conect_db()
            logins = conn.list_logins()
            if logins:
                # Define o número de linhas e colunas da tabela
                self.tableWidget_user_login.clearContents()
                self.tableWidget_user_login.setRowCount(len(logins))
                self.tableWidget_user_login.setColumnCount(len(logins[0]))  # Número de colunas

                # Define os cabeçalhos da tabela manualmente
                header_labels = ["ID", "Usuário", "Senha", "Email"]
                self.tableWidget_user_login.setHorizontalHeaderLabels(header_labels)

                for i, row in enumerate(logins):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget_user_login.setItem(i, j, item)
            else:
                print("Nenhum login encontrado ou erro ao recuperar dados.")

        elif self.radioButton_user.isChecked():
            self.comboBox_tipo.setVisible(True)
            self.txt_email_usre.setVisible(False)
            conn.conect_db()
            users = conn.list_users()
            if users:
                # Define o número de linhas e colunas da tabela
                self.tableWidget_user_login.clearContents()
                self.tableWidget_user_login.setRowCount(len(users))
                self.tableWidget_user_login.setColumnCount(len(users[0]))  # Número de colunas

                # Define os cabeçalhos da tabela manualmente
                header_labels = ["ID", "Usuário", "Senha", "Tipo"]
                self.tableWidget_user_login.setHorizontalHeaderLabels(header_labels)

                for i, row in enumerate(users):
                    for j, value in enumerate(row):
                        if j == 3:  # Se estivermos na coluna "TIPO"
                            # Substitui o valor numérico pelo string correspondente
                            tipo = "User" if value == 0 else "Super-admin"
                            item = QTableWidgetItem(tipo)
                        else:
                            item = QTableWidgetItem(str(value))
                        self.tableWidget_user_login.setItem(i, j, item)
            else:
                print("Nenhum usuário encontrado ou erro ao recuperar dados.")

    #obtém o nome do usuário ao clicar na linha
    def select_line_user_login(self, index):
        conn = Manger_Connect()
        row = index.row()  # Obtém o número da linha do QModelIndex
        item = self.tableWidget_user_login.item(row, 1).text()
        print("Item:", item)
        if self.radioButton_login.isChecked():  # Verifica se o radiobutton está marcado
            conn.conect_db()
            res = conn.select_list_logins(item)
            print(res)
            if res is not None:
                for x in res:
                    id = str(x[0])
                    nome = x[1]
                    senha = x[2]
                    email = x[3]
                    
                    self.txt_id_user_login.setText(id)
                    self.txt_user.setText(nome)
                    self.txt_senha.setText(senha)
                    self.txt_email_usre.setText(email)

        elif self.radioButton_user.isChecked():
            conn.conect_db()
            res = conn.select_list_users(item)
            print(res)
            if res is not None:
                for x in res:
                    id = str(x[0])
                    user = x[1]
                    senha = 'Nova senha'

                    
                    self.txt_id_user_login.setText(id)
                    self.txt_user.setText(user)
                    self.txt_senha.setText(senha)

    def create_new_login_user(self):
        tipo_user = self.comboBox_tipo.currentText()
        user = self.txt_user.text()
        senha = self.txt_senha.text()
        email = self.txt_email_usre.text()

        if self.radioButton_login.isChecked():
            if user == '' or senha == '':
                self.show_error_popup('Atenção!', 'É necessário que todos os campos estejam preenchidos.')
            else:
                try:
                    msg1 = "Login cadastrado com Sucesso!"
                    msg2 = f"Não foi possível cadastrar os dados desejados"

                    self.conect_db()
                    resp = self.create_new_login(user, senha, email)
                    self.msg_popup(resp, msg1, msg2)
                    self.check_user_login()
                except Exception as e:
                    print(e)
                    pass

        elif self.radioButton_user.isChecked():
            if user == '' or senha == '':
                self.show_error_popup('Atenção!', 'É necessário que todos os campos estejam preenchidos.')
            else:
                try:
                    if tipo_user == 'User':
                        tipo = 0 
                    elif tipo_user == 'Super-admin':
                        tipo = 1
                    hash_pass = bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())
                    print(f'senha: {hash_pass}')
                    conn = Manger_Connect()
                    conn.conect_db()
                    resp = conn.create_user(user,hash_pass,tipo)
                    msg1 = f"Usuário cadastrado com sucesso!"
                    msg2 = "Não foi possível registrar os dados"
                    self.msg_popup(resp,msg1,msg2) 
                    self.check_user_login()  
                except Exception as e:
                    print(e)
                    pass

    def alter_login_user(self):
        id_user = self.txt_id_user_login.text()
        tipo_user = self.comboBox_tipo.currentText()
        user = self.txt_user.text()
        senha = self.txt_senha.text()
        email = self.txt_email_usre.text()

        if self.radioButton_login.isChecked():
            if id_user == ''  or user == '' or senha == '':
                self.show_error_popup('Atenção!', 'É necessário que ao menos os campos ID, USER E SENHA\nsejam preenchidos corretamente')
            else:
                try:
                    msg1 = "Login cadastrado com Sucesso!"
                    msg2 = f"Não foi possível cadastrar os dados desejados"

                    self.conect_db()
                    resp = self.alter_login(user=user, senha=senha, email=email,id=id_user)
                    self.msg_popup(resp, msg1, msg2)
                    self.check_user_login()
                except Exception as e:
                    print(e)
                    pass
        elif self.radioButton_user.isChecked():
            if id_user == ''  or user == '' or senha == '':
                self.show_error_popup('Atenção!', 'É necessário que todos os campos estejam preenchidos.')
            else:
                try:
                    if tipo_user == 'User':
                        tipo = 0 
                    elif tipo_user == 'Super-admin':
                        tipo = 1
                    hash_pass = bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())

                    conn = Manger_Connect()
                    conn.conect_db()
                    resp = conn.alter_user(id=id_user,user=user,senha=hash_pass,tipo=tipo,)
                    msg1 = f"Alterado com sucesso!"
                    msg2 = "Não foi possível alterar os dados"
                    self.msg_popup(resp,msg1,msg2)   
                    self.check_user_login()
                except Exception as e:
                    print(e)
                    pass

    def delete_user_login(self):
        id_user = self.txt_id_user_login.text()

        # Verificar se o usuário realmente deseja excluir os dados
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Question)
        confirm_msg.setText("Tem certeza que deseja excluir?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        confirm_msg.setWindowTitle("Confirmação")

        confirm_result = confirm_msg.exec()

        if confirm_result == QMessageBox.Yes:
            if self.radioButton_login.isChecked():
                try:
                    msg1 = "Login deletado com Sucesso!"
                    msg2 = f"Não foi possível deletar os dados desejados"
                    conn = Manger_Connect()
                    conn.conect_db()
                    resp = conn.delete_login(user_id=id_user)
                    self.msg_popup(resp, msg1, msg2)
                    self.check_user_login()
                except Exception as e:
                    print(e)
                    pass
            elif self.radioButton_user.isChecked():
                try:
                    conn = Manger_Connect()
                    conn.conect_db()
                    resp = conn.delete_user(user_id=id_user)
                    msg1 = f"Usuário excluído com sucesso!"
                    msg2 = "Não foi possível deletar os dados"
                    self.msg_popup(resp, msg1, msg2) 
                    self.check_user_login()  
                except Exception as e:
                    print(e)
                    pass

    ##################################   NCM'S ###############################################################################
    # CARREGA OS DADOS DOS ARQUIVOS .JSON
    def carregar_dados_ncm(self):
        try:
            with open('resource\\NCM.json', 'r', encoding='utf-8') as f:
                ncm_data = json.load(f)
                self.nomenclaturas_vigentes = ncm_data['Nomenclaturas']

            with open('resource\\EXPIRED_NCM.json', 'r', encoding='utf-8') as f:
                ncm_data = json.load(f)
                self.nomenclaturas_expiradas = ncm_data['Nomenclaturas']

            ncm_filtradas = self.nomenclaturas_vigentes + self.nomenclaturas_expiradas
            self.atualiza_tabela_ncm(ncm_filtradas)  # Preenche a tabela com os dados carregados

        except FileNotFoundError:
            self.show_error_popup("Erro!", "Arquivos 'NCM.json' e 'EXPIRED_NCM.json' não encontrados.")

    #FILTRA OS DADOS DIGITADOS PELO USUÁRIO
    def filtrar_ncm(self, texto):
        ncm_vigentes_filtradas = [n for n in self.nomenclaturas_vigentes if texto.lower() in n['Codigo'].lower()]
        ncm_expiradas_filtradas = [n for n in self.nomenclaturas_expiradas if texto.lower() in n['Codigo'].lower()]
        ncm_filtradas = ncm_vigentes_filtradas + ncm_expiradas_filtradas
        self.atualiza_tabela_ncm(ncm_filtradas)

    # ATUALIZA A TABELA A MEDIDA QUE O USUÁRIO DIGITA O NCM
    def atualiza_tabela_ncm(self, nomenclaturas):
        self.tableWidget_ncm.clearContents()
        self.tableWidget_ncm.setRowCount(len(nomenclaturas))
        data_atual = datetime.now().date()
        for i, nomenclatura in enumerate(nomenclaturas):
            self.tableWidget_ncm.setItem(i, 0, QTableWidgetItem(nomenclatura['Codigo']))
            self.tableWidget_ncm.setItem(i, 1, QTableWidgetItem(nomenclatura['Descricao']))

            data_vencimento = datetime.strptime(nomenclatura['Data_Fim'], '%d/%m/%Y').date()
            # Verifica se a data de vencimento é anterior à data atual
            if data_vencimento < data_atual:
                # Formata a mensagem de expiração
                mensagem = f"Expirado em: {data_vencimento.strftime('%d/%m/%Y')}"

                # Cria um novo QTableWidgetItem para a mensagem de expiração
                item = QTableWidgetItem(mensagem)
                # Define a cor do texto como vermelho
                item.setForeground(QColor('red'))
                # Define o item na coluna de vencimento
                self.tableWidget_ncm.setItem(i, 2, item)
            else:
                # Preenche a coluna de vencimento com a data normal
                self.tableWidget_ncm.setItem(i, 2, QTableWidgetItem(nomenclatura['Data_Fim']))

    def check_tb_ncm(self):
        if self.radioButton_list_ncm.isChecked():
            # Ocultar elementos quando radioButton_list_ncm estiver selecionado
            self.comboBox_list_datas_ncm.setVisible(False)
            self.bt_buscarncm_database.setVisible(False)
        elif self.radioButton_ncm_dataBases.isChecked():
            # Mostrar elementos quando radioButton_ncm_dataBases estiver selecionado
            self.comboBox_list_datas_ncm.setVisible(True)
            self.bt_buscarncm_database.setVisible(True)
            self.label_siscomex.setVisible(True)

    #FAZ A COMPARAÇÃO DE TODOS OS OS PRODUTOS COM NCM'S INVÁLIDOS E MOSTRA A LISTA EM UMA TABELA
    def buscar_ncm_inDataBases(self):
        from collections import defaultdict
        # INICIA A CONECÇÃO E EXECUTA A QUERY
        query1 = "SELECT CODIGO,NCM, NOME FROM PRODUTO"
        query2 = """SELECT p.id_produto, n.id_ncm, p.nome
                    FROM produto p
                    INNER JOIN ncm n
                    ON p.id_ncm = n.id_ncm
                    ORDER BY p.id_produto"""

        select_data = self.comboBox_list_datas_ncm.currentText()

        ncm_bd = []

        if select_data == 'Etrade': 
            try:  
                self.conn1.cursor.execute(query1)
                ncm_bd = self.conn1.cursor.fetchall()
                print(ncm_bd)
            except Exception as e:
                self.show_error_popup("Erro!",f"Conexão não estabelecida com a Base de Dados!\n{e}")
        elif select_data == 'Hiper':
            try:
                self.conn1.cursor.execute(query2)
                ncm_bd = self.conn1.cursor.fetchall()
            except Exception as e:
                self.show_error_popup("Erro!",f"Conexão não estabelecida com a Base de Dados!\n{e}")

        else:
            ncm_bd = []

        data_atual = datetime.now().date()

        # CARREGA OS DADOS DO ARQUIVO .JSON
        try:
            # Carregar os NCMS expirados do arquivo JSON
            with open('resource\\EXPIRED_NCM.json', 'r', encoding='utf-8') as f:
                expired_ncms_data = json.load(f)
                expired_ncms = expired_ncms_data.get('Nomenclaturas', [])
                
                # Transforma a lista de dicionários em um dicionário onde a chave é o código do NCM
                ncm_dict = defaultdict(dict)
                for ncm_data in expired_ncms:
                    code = ncm_data['Codigo']
                    if code in ncm_dict:
                        current_end_date = datetime.strptime(ncm_dict[code]['Data_Fim'], '%d/%m/%Y').date()
                        new_end_date = datetime.strptime(ncm_data['Data_Fim'], '%d/%m/%Y').date()
                        if new_end_date > current_end_date:
                            ncm_dict[code] = ncm_data
                    else:
                        ncm_dict[code] = ncm_data

                # Converte o dicionário de volta para uma lista de dicionários
                filtered_expired_ncms = list(ncm_dict.values())
        except FileNotFoundError:
            self.show_error_popup("Erro!", "Arquivo 'EXPIRED_NCM.json' não encontrado.")
            filtered_expired_ncms = []

        list_ncm_expired = []
        for ncm in ncm_bd:
            if select_data == 'Etrade':
                ncm_without_dot = ncm[1].replace('.', '')  # Remove o ponto decimal apenas se for Etrade
                formatted_ncm = '{:08}'.format(int(ncm_without_dot))  # Formata para ter oito dígitos
                formatted_ncm = '{}.{}.{}'.format(formatted_ncm[:4], formatted_ncm[4:6], formatted_ncm[6:])  # Aplica a máscara
            else:
                formatted_ncm = ncm[0]  # Use o NCM sem alterações se for Hiper
            for expired_ncm in filtered_expired_ncms:
                if formatted_ncm == expired_ncm.get('Codigo'):
                    data_expiracao = datetime.strptime(expired_ncm.get('Data_Fim'), '%d/%m/%Y').date()
                    if data_expiracao < data_atual:
                        list_ncm_expired.append({
                            'Codigo': ncm[0],
                            'Produto': ncm[2],
                            'NCM': formatted_ncm,  # Usar o NCM formatado ou não formatado conforme a opção selecionada
                            'Data_Fim': data_expiracao.strftime('%d/%m/%Y')
                        })
                        print(f"NCM expirado encontrado no banco de dados: {ncm}")

        # Limpa a tabela antes de adicionar os novos dados
        self.tableWidget_ncm.clearContents()
        self.tableWidget_ncm.setRowCount(0)

        # Adiciona os dados à tabela
        row_position = 0
        for item in list_ncm_expired:
            self.tableWidget_ncm.insertRow(row_position)
            for col, value in enumerate(item.values()):
                self.tableWidget_ncm.setItem(row_position, col, QTableWidgetItem(str(value)))
            row_position += 1

        # Atualiza os cabeçalhos da tabela
        self.tableWidget_ncm.setHorizontalHeaderLabels(['Codigo', 'Produto', 'NCM', 'Data_Fim'])

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def save_data_ncm(self):
        options = QFileDialog.Options()
        path_csv, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Arquivos CSV (*.csv)", options=options)
        if path_csv:
            with open(path_csv, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                # Escreva os cabeçalhos
                headers = ["Codigo", "Descricao", "Vencimento"]
                writer.writerow(headers)
                # Escreva os dados
                for row in range(self.tableWidget_ncm.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget_ncm.columnCount()):
                        item = self.tableWidget_ncm.item(row, column)
                        if item is not None:
                            text = item.text()
                            # Substituir - e -- por espaços em branco
                            text = text.replace('-', '').replace('--', '')
                            row_data.append(text)
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

    def copy_send_Script(self):
        capt_script = self.txt_Scripts.toPlainText()
        self.plainTextEdit.setPlainText(capt_script)
        # Mudar para a página de conexões
        self.pages.setCurrentWidget(self.pg_Data_base)

class ProgressDialog(QDialog):
    def __init__(self,desk, parent=None):
        super().__init__(parent)
        self.setWindowTitle(desk)
        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        self.setModal(True)
        self.progress_bar.setRange(0, 100)
        self.show()

class LoginWindow(QMainWindow, UI_LoginWindow,Manger_Connect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tech Tools")
        appIcon = QIcon(u"img\\TECH NEW LOGO.png")
        self.setWindowIcon(appIcon)
        self.setFixedSize(600, 445)
        self.read_saved_data()
        self.time = QTimer()
        self.time.timeout.connect(self.clean_logs)
        
        path_scripts_tables = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\techtools.db.sql"
        path_data = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\techtools.db"
        update = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\up.db.sql"
        path_txt = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\version.txt"
        path_user = "venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\u.db"
        
        self.bt_atualizacao_login.setVisible(False)
        # Connect signals
        self.bt_login.clicked.connect(self.login_user)
        # Conectar o evento returnPressed dos line edits ao verificador de campos de login
        self.txt_username.returnPressed.connect(self.check_login_fields)
        self.txt_senha_login.returnPressed.connect(self.check_login_fields)
        
        self.verify_existence_data(path_scripts_tables,path_data,update,path_txt,path_user)
        
        version_sys = self.version_sistem_tech()
        self.lb_login_version.setText(str(f'v{version_sys}'))

        self.lb_logs_login.setText(None)

    def clean_logs(self):   
        self.lb_logs_login.clear()

        self.time.stop()

    def logs_login(self,text):
        self.lb_logs_login.clear()
        self.lb_logs_login.setText(str(text))
        self.time.start(5000)




    def version_txt(self,path_txt):
        
        try:
            if os.path.exists(path_txt):
                with open(path_txt, 'r') as r:
                    line = r.readline()
                    for line in r:
                        if line.startswith("db_version:"):
                            v_db = line[len("db_version: "):].strip()
                            print(v_db)
                            return v_db    
        except Exception as e:
            print(f"Erro:\n{e}")

    def versions(self,name_data):
        try:

            conn = sqlite3.connect(name_data)
            cursor = conn.cursor()
            cursor.execute('SELECT VERSION_DB FROM VERSION')
            version = cursor.fetchall()
            conn.close()
            print(f'{version}, uma atualização será necessária.')
            return version
            
        except Exception as e:
            print(f"Erro: {e}")        

    def execut_scripts(self,name_data,update_scripts):
        try:
            with open(update_scripts, 'r',encoding='utf-8') as file:
                scripts_up = file.read()

            conn = sqlite3.connect(name_data)
            cursor = conn.cursor()
            cursor.executescript(scripts_up)
            cursor.execute()
            conn.commit()
            conn.close()
            print("Todos os Scripts foram executados com sucesso!")
            try:
                os.remove(update_scripts)
                print("Arquivo removido com sucesso!")
            except Exception as e:
                    print(f"Erro ao tentar deletar arquivo:\n{e}")
        except Exception as e:
            print(f"Erro: {e}")        

    def verify_existence_data(self, path_scripts, name_data, update, path_txt, path_user):


        try:

            if not os.path.exists(path_user):
                script_user = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\u.db.sql"
                self.create_dataBase_user(path_user)
                self.execut_scripts_creation_userDB(path_user=path_user,datascripts=script_user)


            if not os.path.exists(name_data):
                # Exibir a barra de progresso em uma caixa de diálogo
                progress_dialog = ProgressDialog("Criando o Banco de dados.")
                self.create_dataBase(name_data, progress_dialog) #cria o banco de dados techtools
                self.execut_scripts_creation(path_scripts, name_data)# executa os scripts de dados padrões do sistema
                progress_dialog.accept()  # Fechar a caixa de diálogo após a conclusão
            else:
                # Verifica quais tabelas já existem no banco de dados
                existing_tables = self.get_tables_existents(name_data)
                vs = self.versions(name_data)
                vs_db = self.version_txt(path_txt)
                self.update_version(update)
                
                # Executa os scripts para criar apenas as tabelas que ainda não existem
                self.cria_tabelas_nao_existentes(path_scripts, name_data, existing_tables)
                self.insert_version(conect=name_data) # verifica se a versão do sistema já foi inserida, caso não, faz o insert com os dados da versão
                if vs_db != vs[0][0]:
                    reply = QMessageBox.question(None, "Atenção!", "Há uma nova versão do banco de dados disponível\ndeseja atualizar agora?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        # Exibir a barra de progresso em uma caixa de diálogo
                        progress_dialog = ProgressDialog("Atualizando o banco de dados.")
                        self.update_progress(progress_dialog, name_data, update)
                        progress_dialog.exec_()
                        
                else:
                    pass
            
        except Exception as e:
            print(f"Erro!: {e}")
    
    def update_version(self, update):

        with open(update, 'r') as file:
            v_sys = file.readline()        
            for line in v_sys:
                    if line.startswith("Version_app:"):
                        v = line[len("Version_app: "):].strip()
                        print(f"Versão atual {v}")


    def insert_version(self, conect):
        query = "SELECT version_db, version_system FROM version;"
        update = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\up.db.sql"
        try:
            conn = sqlite3.connect(conect)
            cursor = conn.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            
            if not res:  # Verifica se res é vazio
                # Se res for vazio, executa o INSERT
                conn = sqlite3.connect(conect)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO version (id, version_db, version_system) VALUES (1, '0.0.2', '4.0.3');")
                conn.commit()
                print("Dados da versão inseridos com sucesso!")
            
            else:
                cursor.executescript(update)
                conn.commit()
                print("Os dados da versão já existem.")

        except Exception as e:
            print(f"Erro: {e}")


    def create_dataBase_user(self, path_user):
        try:
            conn = sqlite3.connect(path_user)
            conn.close()
            print("Data base user criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a Data Base: {e}")


    def create_dataBase(self, path_data, progress_dialog):
        try:
            conn = sqlite3.connect(path_data)
            conn.close()
            print("Data base criada com sucesso!")
            progress_value = 0
            while progress_value <= 100:
                progress_dialog.progress_bar.setValue(progress_value)
                QApplication.processEvents()  # Forçar a atualização da interface gráfica
                progress_value += 1
                time.sleep(0.1)  # Intervalo de 100 milissegundos entre atualizações
            progress_dialog.progress_bar.setValue(100)
        except Exception as e:
            print(f"Erro ao criar a Data Base: {e}")

    def update_progress(self, progress_dialog, name_data, update):
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_progress_bar(progress_dialog, name_data, update))
        self.timer.start(500)  # Atualiza a barra de progresso a cada 500 ms

    def update_progress_bar(self, progress_dialog, name_data, update):
        if self.progress_value <= 100:
            progress_dialog.progress_bar.setValue(self.progress_value)
            self.execut_scripts(name_data, update)  # Simula o processamento
            self.progress_value += 1
            QApplication.processEvents()  # Forçar a atualização da interface gráfica
        else:
            self.timer.stop()  # Interrompe o QTimer quando a barra de progresso atinge 100%
            progress_dialog.accept()  # Fecha a caixa de diálogo

    def execut_scripts_creation_userDB(self, path_user, datascripts):
        user1 = 'techtools'
        senha1 = 'techtadm'
        user2 = 'admin'
        senha2 = 'admin' 
        try:
            hash_pass1 = bcrypt.hashpw(senha1.encode('utf-8'), bcrypt.gensalt())
            print(f'senha: {hash_pass1}')
            hash_pass2 = bcrypt.hashpw(senha2.encode('utf-8'), bcrypt.gensalt())
            print(f'senha: {hash_pass2}')

            q1 = "INSERT INTO USERS (user, password, TYPE_US) VALUES (?, ?, ?)"
            q2 = "INSERT INTO USERS (user, password, TYPE_US) VALUES (?, ?, ?)"

            with open(datascripts, 'r', encoding='utf-8') as file:
                scripts_sql = file.read()

            conn = sqlite3.connect(path_user)
            cursor = conn.cursor()
            cursor.executescript(scripts_sql)
            cursor.execute(q1, (user1, hash_pass1, 1))  # Aqui, hash_pass1 já é uma sequência de bytes
            cursor.execute(q2, (user2, hash_pass2, 0))  # Aqui, hash_pass2 já é uma sequência de bytes
            conn.commit()
            conn.close()
            try:
                os.remove(datascripts)
                print("Arquivo removido com sucesso!")
            except Exception as e:
                    print(f"Erro ao tentar deletar arquivo:\n{e}")
            print("Todos os Scripts foram executados com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def execut_scripts_creation(self, path_scripts, name_data):
        try:
            with open(path_scripts, 'r',encoding='utf-8') as file:
                scripts_sql = file.read()

            conn = sqlite3.connect(name_data)
            cursor = conn.cursor()
            cursor.executescript(scripts_sql)
            conn.commit()
            conn.close()
            print("Todos os Scripts foram executados com sucesso!")
            try:
                os.remove(path_scripts)
                print("Arquivo removido com sucesso!")
            except Exception as e:
                    print(f"Erro ao tentar deletar arquivo:\n{e}")
        except Exception as e:
            print(f"Erro: {e}")

    #Pega nomes das tabelas existente no banco de dados
    def get_tables_existents(self,name_data):
        try:
            conn = sqlite3.connect(name_data)
            cursor = conn.cursor()

            #Recupera a lista com os nomes das tabelas da database
            cursor.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table'; ")
            tables_existig = [table[0] for table in cursor.fetchall()]
            print(tables_existig)
            #Fecha a conexão com o banco de dados
            conn.close()
            #Retorna lista  de tabelas
            return tables_existig
        except Exception as e:
            print(f"Erro ao obter lista de tabelas:\n{e}")

    def cria_tabelas_nao_existentes(self,path_scripts, name_data, existing_tables):
        
        try:
            # Lê o conteúdo do arquivo de scripts SQL com encoding UTF-8
            with open(path_scripts, 'r', encoding='utf-8') as file:
                scripts_sql = file.read()

            # Divide o conteúdo do arquivo SQL em comandos individuais
            commands = scripts_sql.split(';')

            # Conecta ao banco de dados
            conn = sqlite3.connect(name_data)
            cursor = conn.cursor()

            # Itera sobre os comandos SQL
            for command in commands:
                # Remove espaços em branco extras e quebras de linha
                command = command.strip()
                if command:
                    # Verifica se a linha contém um comando de criação de tabela
                    if command.startswith("CREATE TABLE IF NOT EXISTS"):
                        # Extrai o nome da tabela e remove espaços em branco
                        table_name = command.split('"')[1].strip()
                        if table_name not in existing_tables:
                            cursor.execute(command)

            # Commit das alterações e fechamento da conexão
            conn.commit()
            conn.close()

            print("Scripts para tabelas inexistentes foram executados com sucesso!")
        except Exception as e:
            print(f"Erro ao executar scripts para tabelas inexistentes: {e}")


    def check_login_fields(self):
        # Verificar se ambos os campos de entrada estão preenchidos
        if self.txt_username.text() and self.txt_senha_login.text():
            # Chamar a função de login
            self.login_user()
        else:           
            # Exibir uma mensagem informando ao usuário que ambos os campos devem ser preenchidos
            QMessageBox.warning(self, "Aviso", "Por favor, preencha ambos os campos de login.")
            


    def cache_user(self,username):
        conn = Manger_Connect()
        conn.conect_db()
        path = "venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\users.txt"
        query = f"SELECT USER,TYPE_US FROM USERS WHERE USER = '{username}'"
        conn.cursor.execute(query)
        res = conn.cursor.fetchall()
        for r in res:
            tipo = r[1]
        with open(path, 'w') as w:
            w.write(f'User: {username}\ntipo: {tipo}')


    def on_login_clicked(self,username,password):
        remember_checked = self.checkBox_lembrar_senha.isChecked()

        path = 'venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\hist.txt'

        try:
            if remember_checked:
                with open(path, 'w') as f:
                    f.write(f'User: {username}\nPass: {password}\nRemember: True')
                print("Dados de login salvos com sucesso!")
            else:
                os.remove(path)
                print("Dados de login excluídos com sucesso!")
        except Exception as e:
            print(f"Erro ao manipular o arquivo de histórico: {e}")

    def read_saved_data(self):
        path = 'venv\\Lib\\site-packages\\_m\\file\\file\\u\\mu\\hist.txt'

        try:
            with open(path, 'r') as file:
                lines = file.readlines()
                saved_user = None
                saved_pass = None
                saved_check = None
                for line in lines:
                    if line.startswith('User:'):
                        saved_user = line.split(': ')[1].strip()
                    elif line.startswith('Pass:'):
                        saved_pass = line.split(': ')[1].strip()
                    elif line.startswith('Remember:'):
                        saved_check = line.split(': ')[1].strip()

                if saved_user and saved_pass and saved_check == 'True':
                    self.checkBox_lembrar_senha.setChecked(True)
                    self.txt_username.setText(saved_user)
                    self.txt_senha_login.setText(saved_pass)

        except FileNotFoundError:
            # Lógica para lidar com o arquivo não existente
            pass

    def login_user(self):
        # Obtém o usuário e a senha digitados pelo usuário
        username = self.txt_username.text()
        password = self.txt_senha_login.text()
        self.checkBox_lembrar_senha
        # Consulta o banco de dados para obter as informações do usuário
        conn = Manger_Connect()
        conn.conect_db()
        comando_user = "SELECT USER,PASSWORD,TYPE_US FROM USERS WHERE USER = ?"
        user_data = (username,)
        conn.cursor.execute(comando_user, user_data)
        stored_user_data = conn.cursor.fetchall()

        if username == '' or password == '':
            self.logs_login("Por favor, preencha ambos os campos de login.")

        else:

            if stored_user_data:
                stored_password_hash = stored_user_data[0][1]  # A senha hash está na segunda posição da tupla
                # Convertendo stored_password_hash para uma string UTF-8
                stored_password_hash_str = stored_password_hash.decode('utf-8')
                self.cache_user(username)
                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash_str.encode('utf-8')):
                    print(f'Sucesso: {stored_password_hash}')
                    # Abra a tela MainWindow após o login bem-sucedido
                    self.open_main_window()
                    self.on_login_clicked(username,password)
                else:
                    self.show_error_popup("Erro de login", "Usuário ou senha incorretos.")
                    self.logs_login("Usuário ou senha incorretos.")
            else:
                self.show_error_popup("Erro de login", "Usuário não encontrado.")
                self.logs_login("Usuário não encontrado.")

            


    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente

