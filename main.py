from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox, filedialog, scrolledtext
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import pandas as pd
import PySimpleGUI as sg
import sqlite3
import psutil
import socket
import pyodbc
import mysql.connector
import webbrowser
import datetime
import csv
import os
import re
import gc
#IMPORTANDO AS FUNÇÕES DO ARQUIVO EXECT.PY
from execut import (
    ib_expert,
    exec_rufus,
    exe_anydesk,
    exec_reloader,
    exec_win11,
    exec_office21,
    exec_driver_rede,
    exec_p_hiper,
    exec_cristal_disk,
    exec_wintohdd,
    exec_ipscaner,
)

#DICIONÁRIO DE FONTES USADAS DENTRO DO PROGRAMA.
st_f = {'f1':('M Hei PRC', 10, 'bold'),'f2':('Helvetica', 8,'bold','italic'),'f3':('Helvetica', 10, 'bold'),'f4':("Helvetica", 12, "bold"),'f5':('Helvetica', 7, 'italic'),'f6':('New', 9,'bold'),'f7':('Arial', 10, 'bold')}

#DICIONÁRIO DE CORES USADAS DENTRO DO PROGRAMA.
# C REPRESENTA CORES
		#CORES	LARANJA			BRANCO		 AZUL ESCURO	AZUL CEU	  VERDE			VERMELHO
c: dict = {'1':'#e69138', '2':'#ffffff','3':'#104e8b', '4':'#f0ffff','5':'#44ab4c','6':'#e32636','7':'#000000'}

links1 = {
        'Hiper.Setup': 'https://downloads.hiper.com.br/Hiper.Setup.exe',
        'E-Trade instalador': 'https://vrsystem.info/files/Install_ETrade.exe',
        'E-Trade versão stable': 'https://vrsystem.info/files/Stable_ETrade.exe',
        'Bancos de Dados dos Estados': 'https://drive.google.com/drive/folders/1hvI1N9nA7PSZx-5HV53qjzI7ekTcJcTf',

        'SQL Server 2014 + SSMS x86': 'https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/ExpressAndTools%2032BIT/SQLEXPRWT_x86_PTB.exe',
        'SQL Server 2014 + SSMS x64': 'https://download.microsoft.com/download/0/1/5/015567C0-E851-4AC6-964F-9BBA9B31D6BC/ExpressAndTools%2064BIT/SQLEXPRWT_x64_PTB.exe',
        'SQL Server® 2019 Express': 'https://www.microsoft.com/pt-br/download/confirmation.aspx?id=101064',



    }

links = {

        # BEMATECH
        'Bematech MP-100S TH 32bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_100_SpoolerDrivers_x86_v4.4.0.3.rar',
        'Bematech MP-100S TH 64bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_100_SpoolerDrivers_x64_v4.4.0.3.rar',
        'Bematech MP-2800 TH 32 bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_2800_SpoolerDrivers_x86_v1.3.rar',
        'Bematech MP-2800 TH 64 bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_2800_SpoolerDrivers_x64_v1.3.rar',
        'Bematech MP-4200 TH 32 bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_4200_SpoolerDrivers_x86_v4.3.1.0.rar',
        'Bematech MP-4200 TH 64 bits': 'https://gbinfosistemas.com.br/atualiza/nv/Impressoras/Bematech_MP_4200_SpoolerDrivers_x64_v4.3.1.0.rar',
        # DARUMA
        'Diebold Todos os Drivers': 'https://dieboldnixdorf.com.br/wp-content/uploads/2021/04/4900c52a69e4dd711601380202f91e8b-1.zip',
        'Daruma DR-800': 'https://drive.google.com/drive/folders/17nZFyaAZsFN-Ub3-kaj2Qg6TSqaIDROf',
        # EPSON
        'Epson TM-T20': 'https://download.epson-biz.com/modules/pos/index.php?page=single_soft&cid=6888&scat=31&pcat=3',
        'Epson TM-T20X': 'https://ftp.epson.com/latin/drivers/pos/APD_601_T20X_WM.zip',
        'Epson TM-T70II': 'https://encr.pw/vhaRp',
        'Epson Térmica TM-T88VII': 'https://epson.com.br/Suporte/Ponto-de-venda/Impressoras-térmicas/Epson-TM-T88VII-Series/s/SPT_C31CJ57052',
        'Epson L375': 'https://ftp.epson.com/latin/drivers/inkjet/L375_Lite_LA.exe',
        'Epson L1250': 'https://ftp.epson.com/latin/drivers/inkjet/L1250_Lite_LA.exe',
        'Epson L3110': 'https://ftp.epson.com/latin/drivers/Multi/l3110/L3110_Lite_LA.exe',
        'Epson L3210': 'https://ftp.epson.com/latin/drivers/inkjet/L3210_Lite_LA.exe',
        'Epson L3250': 'https://ftp.epson.com/latin/drivers/inkjet/L3250_L3251_Lite_LA.exe',
        'Epson L3251': 'https://epson.com.br/c/Epson-L3251/s/SPT_C11CJ67302',
        'Epson L3252': 'https://www.epson.co.in/Support/Printers/All-In-One/L-Series/Epson-L3252/s/SPT_C11CJ67511',
        'Epson L4160': 'https://ftp.epson.com/latin/drivers/inkjet/L4160_Lite_LA.exe',
        'Epson L4260': 'https://ftp.epson.com/latin/drivers/inkjet/L4260_Lite_LA.exe',
        # ELGIN
        'Elgin i7/i9': 'https://www.elgin.com.br/assets/arquivos/imgCard_4ce638a5-22e5-4a0d-a820-0108152ced91_imgCard_3969ab8d-70ab-4b53-ac90-d84cc55ddd70_ELGIN%20i9%20Printer%20Driver_v-1.7.3.rar',

        # Impressoras HP
        'HP DeskJet 2774': 'https://arquivos.blogdainformatica.com.br/drivers/impressoras/hp/hp-deskjet-ink-2770/HPEasyStart-13.6.5-DJ2700_51_4_4865_1_Webpack.exe?md5=7Rcm0COquWIQHQax9e1pLA&expires=1681620578',
        'HP Ink Tank Wireless 416': 'https://ftp.ext.hp.com/pub/softlib/software13/printers/ITW410/Full_Webpack-45.4.2608-ITW410_Full_Webpack.exe',
        # ARQUIVOS DE INSTALAÇÃO
        'Samsung ML-2160': 'https://ftp.hp.com/pub/softlib/software13/printers/SS/SL-M3370FD/SamsungUniversalPrintDriver3.exe',
        # impressoras Xerox
        'Xerox Phaser 3020': 'https://www.support.xerox.com/pt-br/product/phaser-3020/downloads?language=pt_BR#',
        # Impressoras Zebra
        'Zebra Z800': 'https://www.zebra.com/br/pt/support-downloads/eula/unrestricted-eula.7b8a235653193b4c72c440110c25661656f56f5180957c98e7c0bc2144149cd156a1bc6e684725abae8eaa3b64ee1090a63134434792cf7fe7ebd953120a60cd367633fe9f513f4ae43f722b47f328b04e84f768a150ebe0.html#',

        # Impressoras de Etiquetas
        'Argox All Driver': 'https://drive.google.com/uc?id=134HjCgrHHWQ9CArgcSUUowsK0H3nrxR6&export=download',
        'Elgin L42 PRO FULL': 'https://l1nq.com/N6Ju1',

        'Zebra ZD420': 'https://l1nq.com/lS9Ok',

        'Zebra ZD421': 'https://l1nq.com/lS9Ok',

        'Zebra ZD621': 'https://l1nq.com/lS9Ok',

        'Zebra ZD621R RFID': 'https://l1nq.com/lS9Ok',

        'Zebra GK420T': 'https://l1nq.com/xSIlz',

        'Bematech LB-1000': 'https://l1nq.com/6ASQV',
    }
arquivos = ["Advanced_IP_Scanner", "Driver's de Rede", 'Pré-Implantação Hiper', "AnyDesk", "Rufus Botável", 'Crystal Disk Info', 'WinToHDD_Clonar HD','Hiper.Setup', 'E-Trade instalador', 'E-Trade versão stable', 'Bancos de Dados dos Estados', 'SQL Server 2014 + SSMS x86', 'SQL Server 2014 + SSMS x64', 'SQL Server 2019 Express']

impres = ['--Impressoras de Cupons--', 'Bematech MP-100S TH 32bits', 'Bematech MP-100S TH 64bits', 'Bematech MP-2800 TH 32 bits', 'Bematech MP-2800 TH 64 bits', \
                               'Bematech MP-4200 TH 32 bits', 'Bematech MP-4200 TH 64 bits', 'Diebold Todos os Drivers', 'Daruma DR-800', 'Epson TM-T20', 'Epson TM-T20X', 'Epson TM-T70II', 'Epson Térmica TM-T88VII', 'Epson L375', \
                               'Epson L1250', 'Epson L3110', 'Epson L3210', 'Epson L3250', 'Epson L3251', 'Epson L3252', 'Epson L4160', 'Epson L4260', 'Elgin i7/i9', \
                               'HP DeskJet 2774', 'HP Ink Tank Wireless 416', 'Samsung ML-2160', 'Xerox Phaser 3020', \
                               '--Impressoras de Etiquetas--', 'Argox All Driver', 'Bematech LB-1000', 'Elgin L42 PRO FULL', 'Zebra ZD420', 'Zebra ZD421', 'Zebra GK420T', 'Zebra ZD621', 'Zebra ZD621R RFID', 'Zebra Z800']
# Query's que serão responsáveis pelas consultas no banco de dados
#NÃO  CONSEGUI TER ACESSO A ESSAS QUERYS A PARTIR DE OUTRO ARQUIVO
clientes = ("""SELECT
        DISTINCT
        CASE
        WHEN tipo_entidade = 1 THEN 'Pessoa física'
        WHEN tipo_entidade = 2 THEN 'Pessoa jurídica'
        WHEN tipo_entidade = 3 THEN 'Pessoa simplificada'
        END AS 'Tipo cliente',
        E.NOME,E.LOGRADOURO,E.NUMERO_ENDERECO,
        E.BAIRRO,E.COMPLEMENTO,E.CEP,
        E.FONE_PRIMARIO_DDD,E.FONE_PRIMARIO_NUMERO,
        F.CPF,F.RG,J.CNPJ,J.IE,J.NOME_FANTASIA,
        C.NOME AS CIDADE,C.UF	   
        FROM ENTIDADE E
        LEFT JOIN PESSOA_FISICA F
        ON E.ID_ENTIDADE = F.ID_ENTIDADE
        LEFT JOIN PESSOA_JURIDICA J
        ON E.ID_ENTIDADE = J.ID_ENTIDADE
        LEFT JOIN CIDADE C
        ON E.ID_CIDADE = C.ID_CIDADE
        ORDER BY  [Tipo cliente] DESC
        """)

fornecedor = (""" SELECT
        t1.nome AS 'Nome fornecedor',
        CASE
        WHEN t3.ie <> '' THEN t3.ie
        WHEN t4.ie <> '' THEN t4.ie
        WHEN t3.ie = ' ' AND t1.tipo_entidade = 1 THEN 'Sem I.E'
        WHEN t4.ie = ' ' AND t1.tipo_entidade = 2 THEN 'Sem I.E'
        WHEN t1.tipo_entidade = 3 THEN 'Sem I.E'
        END AS 'Inscrição estadual',
        codigo AS 'Código',
        CASE
        WHEN fone_primario_ddd IS NOT NULL THEN '(' + fone_primario_ddd + ')' +' '+
        fone_primario_numero
        WHEN fone_secundario_ddd IS NOT NULL THEN '(' + fone_secundario_ddd + ')' +' '+
        fone_secundario_numero
        WHEN fone_secundario_ddd IS NULL AND fone_primario_ddd IS NULL THEN 'Sem telefone
        cadastrado'
        END AS 'Telefone',
        ISNULL(t2.nome + ' - ' + t2.uf, 'Sem cidade/UF cadastrada') AS 'Localidade',
        CASE
        WHEN t1.logradouro = '' THEN 'Sem logradouro cadastrado'
        WHEN t1.logradouro <> '' THEN t1.logradouro
        END AS 'Logradouro',
        CASE
        WHEN ISNUMERIC(t1.numero_endereco) = 0 THEN 'Sem número cadastrado'
        WHEN ISNUMERIC(t1.numero_endereco) = 1 THEN t1.numero_endereco
        END AS 'Número endereço',
        CASE
        WHEN t1.bairro = ' ' THEN 'Sem bairro cadastrado'
        WHEN t1.bairro <> '' THEN t1.bairro
        END AS 'Bairro',
        CASE
        WHEN tipo_entidade = 1 THEN t3.cpf + ' - ' +'CPF'
        WHEN tipo_entidade = 2 THEN t4.cnpj + ' - ' + 'CNPJ'
        WHEN tipo_entidade NOT IN (1,2) THEN 'Sem CPF ou CNPJ'
        END AS 'CPF/CNPJ',
        CASE
        WHEN flag_fornecedor = 1 THEN 'É fornecedor'
        END AS 'Tipo'
        FROM entidade t1
        LEFT JOIN cidade t2 ON t1.id_cidade = t2.id_cidade
        LEFT JOIN pessoa_fisica t3 ON t1.id_entidade = t3.id_entidade
        LEFT JOIN pessoa_juridica t4 ON t1.id_entidade = t4.id_entidade
        WHERE t1.flag_fornecedor = 1 AND t1.excluido = 0""")

produtos = ("""SELECT
        t1.codigo,
        COALESCE(t2.codigo_barras, '') AS codigo_barras,
        t1.referencia_interna_produto,
        t1.nome AS nome_produto,
        t9.codigo AS codigo_fornecedor,
        t4.sigla as sigla_unidade_medida,
        t6.quantidade as Estoque,
        t1.preco_aquisicao AS precoFornecedor,
        t1.preco_custo AS preço_de_custo,
        t1.preco_minimo_venda,
        t1.preco_venda,
        t3.id_ncm AS NCM,
        isnull(cast(t5.id_situacao_tributaria_icms AS VARCHAR), '') AS Codigo_situacao_tributaria_ICMS,
        isnull(cast(t5.id_situacao_tributaria_simples_nacional AS VARCHAR), '') AS CSOSN,
        isnull(cast(t5.aliquota_icms AS VARCHAR), '') AS AliquotaICMS,
        isnull(cast(t5.percentual_reducao_base_icms AS VARCHAR), '') AS ReducaoICMS,
        isnull(cast(t5.mva AS VARCHAR), '') AS MVA
        FROM produto t1
        LEFT JOIN produto_sinonimo t2 ON t1.id_produto = t2.id_produto
        LEFT JOIN ncm t3 ON t1.id_ncm = t3.id_ncm
        LEFT JOIN unidade_medida t4 ON t1.id_unidade_medida = t4.id_unidade_medida
        LEFT JOIN regra_tributacao_icms_personalizada t5 ON t1.id_produto = t5.id_produto
        LEFT JOIN saldo_estoque t6 ON t1.id_produto = t6.id_produto
        LEFT JOIN entidade t9 ON t1.id_entidade_fornecedor = t9.id_entidade
        WHERE t1.codigo <> 1
        --GROUP BY t6.id_produto, t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade --t1.codigo, t2.codigo_barras, t1.referencia_interna_produto, t1.nome, t9.codigo, t4.sigla, t6.quantidade,
        ORDER BY t1.codigo""")

#CRIA VÁRIOS OBJETOS DE IMAGENS QUE SÃO MOSTRADAS NO PROGRAMA	
class Img():
	def __init__(self):
            image1 = Image.open("image\\ibExp.png")
            desired_size1 = (50, 50)  # Tamanho desejado
            resized_image1 = image1.resize(desired_size1)
            self.ibexpert = ImageTk.PhotoImage(resized_image1)

            image2 = Image.open("image\\util.png")
            desired_size2 = (30, 30)  # Tamanho desejado
            resized_image2 = image2.resize(desired_size2)
            self.ultili = ImageTk.PhotoImage(resized_image2)

            image3 = Image.open("image\\home.png")
            desired_size3 = (30, 30)  # Tamanho desejado
            resized_image3 = image3.resize(desired_size3)
            self.home = ImageTk.PhotoImage(resized_image3)

            image4 = Image.open("image\\users.png")
            desired_size4 = (30, 30)  # Tamanho desejado
            resized_image4 = image4.resize(desired_size4)
            self.users = ImageTk.PhotoImage(resized_image4)

            image5 = Image.open("image\\TECHTOOL_LOGO.png")
            desired_size5 = (350, 350)  # Tamanho desejado
            resized_image5 = image5.resize(desired_size5)
            self.tech = ImageTk.PhotoImage(resized_image5)


            # image6 = Image.open("image\\save.png")
            # desired_size6 = (30, 30)  # Tamanho desejado
            # resized_image6 = image6.resize(desired_size6)
            # self.save = ImageTk.PhotoImage(resized_image6)


            image7 = Image.open("image\\db.png")
            desired_size7 = (30, 30)  # Tamanho desejado
            resized_image7 = image7.resize(desired_size7)
            self.mundo = ImageTk.PhotoImage(resized_image7)


            # image8 = Image.open("image\\close.png")
            # desired_size8 = (30, 30)  # Tamanho desejado
            # resized_image8 = image8.resize(desired_size8)
            # self.close = ImageTk.PhotoImage(resized_image8)

#REALIZA A CONEXÃO COM BANCOS DE DADOS.
class Conexao():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cursor = None  # Inicializa o atributo cursor
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server +
                                  ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        # abre a conexão com o banco de dados
        self.cursor = self.conn.cursor()

    def conect_sqlserver(self):
        try:
            self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server +
                                  ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            if self.cursor:
                messagebox.showinfo("Conectado!", "Conectado com sucesso")
        except Exception as e:
            messagebox.showerror(
                f"Não foi possível conectar ao banco de dados! \n MOTIVO DO ERRO:" + str(e))


    def conect_my_sql(self):
        database = db_entry.get()  # Obter o valor do Entry de database
        username = user_entry.get()  # Obter o valor do Entry de usuário
        password = password_entry.get()  # Obter o valor do Entry de senha
        try:
            # estabelece a conexão
            conn = mysql.connector.connect(
                user=username,
                password=password,
                host='localhost',
                database=database
            )

            # abre a conexão com o banco de dados
            self.cursor = conn.cursor()
            if self.cursor:
                messagebox.showinfo("Conectado!", "Conectado com sucesso")

        except mysql.connector.Error as e:
            messagebox.showerror(
                f"Não foi possível conectar ao banco de dados! \n MOTIVO DO ERRO:" + str(e))

class Sqlite_Conn():
    def __init__(self):

         # Conecta-se ao banco de dados (ou cria um novo se não existir)
        self.conn = sqlite3.connect('resources\\file_db\\file\\bd\\manager.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM MANAGER_PASS")
        self.result = self.cursor.fetchall()

    def seach_data_page4(self):
        # Executa a pesquisa
        search_query = seach_dados.get()
        if search_query and bt_seach_dados:
            self.cursor.execute("SELECT id, nome, senha, email, obs FROM manager_pass WHERE id = ? OR nome = ? OR email = ?", (search_query, search_query, search_query))
            search_results = self.cursor.fetchall()
            
            if search_results:
                id_entry.config(state=tk.NORMAL)
                id_entry.delete(0, tk.END)
                id_entry.insert(0, search_results[0][0])
                id_entry.config(state=tk.DISABLED)
                
                manager_user_et.delete(0, END)
                if len(search_results[0]) >= 2:
                    manager_user_et.insert(0, search_results[0][1])
                
                manager_pass_et.delete(0, END)
                if len(search_results[0]) >= 3:
                    manager_pass_et.insert(0, search_results[0][2])
                
                email_entry.delete(0, END)
                if len(search_results[0]) >= 4:
                    email_entry.insert(0, search_results[0][3])
                
                obs_entry.delete(0, END)
                if len(search_results[0]) >= 5:
                    obs_entry.insert(0, search_results[0][4])

                # Limpa a Treeview
                tree.delete(*tree.get_children())

                # Adiciona os resultados da pesquisa à Treeview
                for row in search_results:
                    tree.insert("", "end", values=row)
            else:
                # Caso não haja resultados da pesquisa, limpe todos os campos
                id_entry.config(state=tk.NORMAL)
                id_entry.delete(0, tk.END)
                id_entry.config(state=tk.DISABLED)

                manager_user_et.delete(0, END)
                manager_pass_et.delete(0, END)
                email_entry.delete(0, END)
                obs_entry.delete(0, END)

        if search_query == '' and bt_seach_dados:
            self.cursor.execute("SELECT id ,nome, senha, email, obs FROM manager_pass")
            search_results = self.cursor.fetchall()
            # id_entry.config(state=tk.NORMAL)  # Habilita o campo temporariamente
            # id_entry.delete(0, tk.END)  # Limpa o campo de entrada
            # id_entry.insert(0, search_results[0][0])  # Insere o valor do ID obtido
            # id_entry.config(state=tk.DISABLED)  # Desabilita o campo novamente
            # manager_user_et.delete(0, END)
            # manager_user_et.insert(0, search_results[0][1])
            # manager_pass_et.delete(0 , END)
            # manager_pass_et.insert(0, search_results[0][2])
            # obs_entry.delete(0, END)
            # obs_entry.insert(0, search_results[0][3])
            # email_entry.delete(0, END)
            # email_entry.insert(0, search_results[0][2])
            
            # Limpa a Treeview
            tree.delete(*tree.get_children())

            # Adiciona os resultados da pesquisa à Treeview
            for row in search_results:
                tree.insert("", "end", values=row)

    def add_manager_pass(self):
        manager_pass = manager_pass_et.get()
        manager_user = manager_user_et.get()
        email = email_entry.get()
        obs = obs_entry.get()

        if manager_user == '' or manager_pass == '':
            messagebox.showinfo("Atenção", "Para cadastrar um novo usuário, é necessário preencher os campos obrigatórios (Nome e Senha).")
        else:
            if new_user_var.get() == 0 and alt_user_var.get() == 0:
                messagebox.showwarning("Atenção!", "Uma das opções deve ser marcada, (Novo Usuário ou Gerenciador de logins).\nVerifique e tente novamente!")
            else:
                try:
                    if new_user_var.get() == 1:
                        manager_pass = manager_pass_et.get()
                        manager_user = manager_user_et.get()
                        query_salvar4 = f"INSERT INTO manager_pass(nome, senha) VALUES ('{manager_user}','{manager_pass}')"
                        self.cursor.execute(query_salvar4)
                        self.conn.commit()
                        messagebox.showinfo("Sucesso!", "Usuário cadastrado com sucesso!")
                    
                    if alt_user_var.get() == 1:
                        manager_pass = manager_pass_et.get()
                        manager_user = manager_user_et.get()
                        email = email_entry.get()
                        obs = obs_entry.get()
                        query_salvar5 = f"INSERT INTO manager_pass (nome, senha, email, obs) VALUES ('{manager_user}','{manager_pass}','{email}','{obs}');"
                        self.cursor.execute(query_salvar5)
                        self.conn.commit()
                        messagebox.showinfo("Sucesso!", "Cadastro realizado com sucesso!")
                except Exception as e:
                    messagebox.showerror("Error!", f"Não foi possível cadastrar um novo usuário!\n{e}")

    def alter_user(self):
        user = manager_user_et.get()
        senha = manager_pass_et.get()
        email = email_entry.get()
        obs = obs_entry.get()
        id_entry4 = id_entry.get()
        try:
            query_alter = f"UPDATE manager_pass SET nome='{user}', senha='{senha}', email='{email}', obs='{obs}' WHERE id='{id_entry4}'"
            sqllite.cursor.execute(query_alter)
            sqllite.conn.commit()
            messagebox.showinfo("Sucesso!", "Dados Alterados com sucesso!")
        except Exception as e:
            messagebox.showerror("Error!", f"Não foi possível alterar os dados inseridos!\n{e}")

    def exclude_data4(self):
        id_entry4 = id_entry.get()
        try:
            query_exclude = f"DELETE FROM manager_pass WHERE ID= '{id_entry4}'"
            sqllite.cursor.execute(query_exclude)
            messagebox.showinfo("Sucesso!", "Dados do excluídos  com sucesso!")
            sqllite.conn.commit()
        except Exception as e:
                messagebox.showerror("Error!", f"Não foi possível excluir os dados inseridos!\n{e}")

class Execut():
	def __init__(self):
		pass
	def ibexpert(self):
		ib_expert()
	def rufus(self):
		exec_rufus()
	def anydesk(self):
		exe_anydesk()
	def reloader(self):
		exec_reloader()
	def activ_win11(self):
		exec_win11()
	def office21(self):
		exec_office21()
	def dvr_rede(self):
		exec_driver_rede()
	def hiper_pre(self):
		exec_p_hiper()
	def cristal_disk(self):
		exec_cristal_disk()
	def winhdd(self):
		exec_wintohdd()
	def ipscaner(self):
		exec_ipscaner()

def file_list():
    executor = Execut()  # Renomeia a variável para evitar colisão de nomes
    selected_value = aq_inst.get()  # Obtém o valor selecionado no Combobox
    if selected_value == "Advanced_IP_Scanner" and bt_baixar_file:
        executor.ipscaner()
    elif selected_value == "Driver's de Rede" and bt_baixar_file:
        executor.dvr_rede()
    elif selected_value == "Pré-Implantação Hiper" and bt_baixar_file:
        executor.hiper_pre()
    elif selected_value == 'AnyDesk' and bt_baixar_file:
        executor.anydesk()
    elif selected_value == 'Rufus Botável' and bt_baixar_file:
        executor.rufus()
    elif selected_value == 'Crystal Disk Info' and bt_baixar_file:
        executor.cristal_disk()
    elif selected_value == 'WinToHDD_Clonar HD' and bt_baixar_file:
        executor.winhdd()
    elif selected_value == 'Hiper.Setup' and bt_baixar_file:
        webbrowser.open(links1['Hiper.Setup'])
    elif selected_value == 'E-Trade instalador' and bt_baixar_file:
        webbrowser.open(links1['E-Trade instalador'])
    elif selected_value == 'E-Trade versão stable' and bt_baixar_file:
        webbrowser.open(links1['E-Trade versão stable'])
    elif selected_value == 'Bancos de Dados dos Estados' and bt_baixar_file:
        webbrowser.open(links1['Bancos de Dados dos Estados'])
    elif selected_value == 'SQL Server 2014 + SSMS x86' and bt_baixar_file:
        webbrowser.open(links1['SQL Server 2014 + SSMS x86'])
    elif selected_value == 'SQL Server 2014 + SSMS x64' and bt_baixar_file:
        webbrowser.open(links1['SQL Server 2014 + SSMS x64'])
    elif selected_value == 'SQL Server 2019 Express' and bt_baixar_file:
        webbrowser.open(links1['SQL Server® 2019 Express'])

def list_printers():
    impressoras = prints.get()

    if impressoras == 'Bematech MP-100S TH 32bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-100S TH 32bits'])

    elif impressoras == 'Bematech MP-100S TH 64bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-100S TH 64bits'])

    elif impressoras == 'Bematech MP-2800 TH 32 bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-2800 TH 32 bits'])

    elif impressoras == 'Bematech MP-2800 TH 64 bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-2800 TH 64 bits'])

    elif impressoras == 'Bematech MP-4200 TH 32 bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-4200 TH 32 bits'])

    elif impressoras == 'Bematech MP-4200 TH 64 bits' and bt_baixar_print:
        webbrowser.open(links['Bematech MP-4200 TH 64 bits'])
    
    elif impressoras == 'Diebold Todos os Drivers' and bt_baixar_print:
        webbrowser.open(links['Diebold Todos os Drivers'])
    
    elif impressoras == 'Daruma DR-800' and bt_baixar_print:
        webbrowser.open(links['Daruma DR-800'])
    
    elif impressoras == 'Elgin i7/i9' and bt_baixar_print:
        webbrowser.open(links['Elgin i7/i9'])
    
    elif impressoras == 'HP DeskJet 2774' and bt_baixar_print:
        webbrowser.open(links['HP DeskJet 2774'])

    elif impressoras == 'HP Ink Tank Wireless 416' and bt_baixar_print:
        webbrowser.open(links['HP Ink Tank Wireless 416'])
        
    elif impressoras == 'Samsung ML-2160' and bt_baixar_print:
        webbrowser.open(links['Samsung ML-2160'])

    elif impressoras == 'Xerox Phaser 3020' and bt_baixar_print:
        webbrowser.open(links['Xerox Phaser 3020'])

    elif impressoras == 'Zebra Z800' and bt_baixar_print:
        webbrowser.open(links['Zebra Z800'])

    elif impressoras == 'Argox All Driver' and bt_baixar_print:
        webbrowser.open(links['Argox All Driver'])

    elif impressoras == 'Elgin L42 PRO FULL' and bt_baixar_print:
        webbrowser.open(links['Elgin L42 PRO FULL'])

    elif impressoras == 'Bematech LB-1000' and bt_baixar_print:
        webbrowser.open(links['Bematech LB-1000'])

    elif impressoras == 'Zebra GK420T' and bt_baixar_print:
        webbrowser.open(links['Zebra GK420T'])

    elif impressoras == 'Zebra ZD621R RFID' and bt_baixar_print:
        webbrowser.open(links['Zebra ZD621R RFID'])

    elif impressoras == 'Zebra ZD621' and bt_baixar_print:
        webbrowser.open(links['Zebra ZD621'])

    elif impressoras == 'Zebra ZD421' and bt_baixar_print:
        webbrowser.open(links['Zebra ZD421'])

    elif impressoras == 'Zebra ZD420' and bt_baixar_print:
        webbrowser.open(links['Zebra ZD420'])

    elif impressoras == 'Epson L4260' and bt_baixar_print:
        webbrowser.open(links['Epson L4260'])

    elif impressoras == 'Epson L4160' and bt_baixar_print:
        webbrowser.open(links['Epson L4160'])

    elif impressoras == 'Epson L3252' and bt_baixar_print:
        webbrowser.open(links['Epson L3252'])

    elif impressoras == 'Epson L3251' and bt_baixar_print:
        webbrowser.open(links['Epson L3251'])

    elif impressoras == 'Epson L3250' and bt_baixar_print:
        webbrowser.open(links['Epson L3250'])

    elif impressoras == 'Epson L3210' and bt_baixar_print:
        webbrowser.open(links['Epson L3210'])

    elif impressoras == 'Epson L3110' and bt_baixar_print:
        webbrowser.open(links['Epson L3110'])

    elif impressoras == 'Epson L1250' and bt_baixar_print:
        webbrowser.open(links['Epson L1250'])

    elif impressoras == 'Epson L375' and bt_baixar_print:
        webbrowser.open(links['Epson L375'])

    elif impressoras == 'Epson Térmica TM-T88VII' and bt_baixar_print:
        webbrowser.open(links['Epson Térmica TM-T88VII'])

    elif impressoras == 'Epson TM-T70II' and bt_baixar_print:
        webbrowser.open(links['Epson TM-T70II'])

    elif impressoras == 'Epson TM-T20X' and bt_baixar_print:
        webbrowser.open(links['Epson TM-T20X'])

    elif impressoras == 'Epson TM-T20' and bt_baixar_print:
        webbrowser.open(links['Epson TM-T20'])

#REALIZA A BUSCA POR SERVIDORES DE BANCO DE DADOS ATIVOS NO MOMENTO.
def lists_servers():
	# Lista de servidores de banco de dados e seus apelidos
    servidores = {'mysqld.exe': 'MySQL', 'sqlservr.exe': 'SQL Server',
                    'fbserver.exe': 'Firebird Server', 'mongodb': 'MongoDB'}

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

#BUSCA PELA QUERY CLIENTE, FORNECEDOR, PRODUTOS E BAIXA O ARQUIVO CSV.
def seach_sql():
	server = entry_server.get()
	database = db_entry.get()
	username = user_entry.get()
	password = password_entry.get()
	conn = Conexao(server, database, username, password)

	if check_1_var.get() == 1:  # Use o método get() para verificar se o checkbox está marcado
		conn.cursor.execute(clientes)
		lines1 = conn.cursor.fetchall()
        # Abre a caixa de diálogo para salvar o arquivo CSV
        # Tk().withdraw()  # Esconde a janela principal do tkinter
		filename = filedialog.asksaveasfile(defaultextension='.csv',filetypes=[("CSV Files", "*.csv")])

        # verifica se o usuário selecionou um arquivo
		if filename is not None:

            # obtém o arquivo escolhido
			nome_do_arquivo1 = filename.name

            # cria o objeto csv.writer
			with (open(nome_do_arquivo1, 'w', newline='')) as f:

				writer = csv.writer(f, delimiter=';')
					# Escreve os cabeçalhos
				writer.writerow(['TIPO', 'NOME', 'LOGRADOURO', 'NUMERO_ENDERECO', 'BAIRRO', 'COMPLEMENTO', 'CEP',
											'FONE_PRIMARIO_DDD', 'FONE_PRIMARIO_NUMERO', 'CPF', 'RG', 'CNPJ', 'IE', 'NOME_FANTASIA', 'CIDADE', 'UF'])
                # Escreve os dados no arquivo CSV usando o método writerows
				writer.writerows(lines1)
                    # Fecha o aquivo csv
				filename.close()
                # Fecha a conexão
				messagebox.showinfo("Suecesso!", "Arquivo CSV gerado com sucesso!")
				conn.cursor.close()
		else:
			messagebox.showerror("Error","Erro ao tentar gerar o arquivo CSD.\nTente novamente mais tarde.")
			conn.cursor.close()

            # Obtém os Dados de clientes

	elif check_2_var.get() == 1:
		conn.cursor.execute(fornecedor)
		lines1 = conn.cursor.fetchall()

                # Abre a caixa de diálogo para salvar o arquivo CSV
                # Tk().withdraw()  # Esconde a janela principal do tkinter
		filename = filedialog.asksaveasfile(defaultextension='.csv',filetypes=[("CSV Files", "*.csv")])

                # verifica se o usuário selecionou um arquivo
		if filename is not None:

            # obtém o arquivo escolhido
			nome_do_arquivo = filename.name

                    # cria o objeto csv.writer
			with (open(nome_do_arquivo, 'w', newline='')) as f:

				writer = csv.writer(f, delimiter=';')
                # Escreve os cabeçalhos
				writer.writerow(['NOME_FORNECEDOR', 'INCRICAO_ESTADUAL', 'CODIGO', 'TELEFONE',
                                        'CIDADE', 'ENDERECO', 'NUMERO', 'BAIRRO', 'CPF/CNPJ', 'TIPO'])
                # Escreve os dados no arquivo CSV usando o método writerows
				writer.writerows(lines1)
                # Fecha o aquivo csv
				filename.close()
				messagebox.showinfo("Suecesso!", "Arquivo CSV gerado com sucesso!")
				conn.cursor.close()
		else:
			messagebox.showerror("Error","Erro ao tentar gerar o arquivo CSD.\nTente novamente mais tarde.")
			conn.cursor.close()

	elif check_3_var.get() == 1:
		conn.cursor.execute(produtos)
		lines1 = conn.cursor.fetchall()

        # Abre a caixa de diálogo para salvar o arquivo CSV
        # Tk().withdraw()  # Esconde a janela principal do tkinter
		filename = filedialog.asksaveasfile(defaultextension='.csv',filetypes=[("CSV Files", "*.csv")])

        # verifica se o usuário selecionou um arquivo
		if filename is not None:

            # obtém o arquivo escolhido
			nome_do_arquivo = filename.name

            # cria o objeto csv.writer
			with (open(nome_do_arquivo, 'w', newline='')) as f:
				writer = csv.writer(f, delimiter=';')
				writer.writerow(['CODIGO', 'CODIGO_BARRAS', 'REFERENCIA_INTERNA', 'NOME_PRODUTO', 'COD_FORNECEDOR', 'UN_MEDIDA', 'ESTOQUE', 'PRECO_FORNECEDOR',
                                        'PRECO_CUSTO', 'PRECO_MINIMO_VENDA', 'PRECO_VENDA', 'NCM', 'COD_SITUACAO T._ICM', 'CSOSN', 'ALICOTA_ICMS', 'REDUCAO_ICMS', 'MVA'])
                # Escreve os dados no arquivo CSV usando o método writerows
				writer.writerows(lines1)
                # Fecha o aquivo csv
				filename.close()
				messagebox.showinfo("Suecesso!", "Arquivo CSV gerado com sucesso!")
				conn.cursor.close()
		else:
			messagebox.showerror("Error","Erro ao tentar gerar o arquivo CSD.\nTente novamente mais tarde.")
			conn.cursor.close()

#OBTÉM A VERSÃO ATUAL DO SISTEMA
def obter_versao_atual():
    # Lê a versão atual do programa do arquivo "version.txt"
    versao = os.path.join(os.path.dirname(
        __file__), 'version.txt')

    with open(versao, "r") as f:
        versao_atual = f.read().strip()

    return versao_atual

#FAZ CONEXÃO COM O BANCO DE DADOS ESCOLHIDO
def conectar():
	global server,database,username,password
	server = entry_server.get()
	database = db_entry.get()
	username = user_entry.get()
	password = password_entry.get()
	conection = Conexao(server, database, username, password)
	selected_db = op_dbs.get()
	if selected_db == "SQL Server":
		conection.conect_sqlserver()

	if selected_db == 'MySQL':
		sqllite.conect_my_sql()

#MOSTRA A LISTA DE TABELAS DISPONÍVEIS
def view_tables():
    conection = Conexao(server, database, username, password)
    server = entry_server.get()
    database = db_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    
    conection.cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_CATALOG='{database}'")
    resultados = conection.cursor.fetchall()
    lista_tabelas = [tabela[0] for tabela in resultados]

    root = Tk()
    root.title("Mostrar Tabelas Disponíveis")
    root.geometry("350x350")
    
    root_frame = tk.Frame(root, background=c['3'], width=390, height=300)
    root_frame.place_configure(x=1,y=1)


    output_text = scrolledtext.ScrolledText(root_frame, width=50, height=15)  # Move this line here
    output_text.grid(column=0, row=1, pady=10)

    tabela_formatada = '\n'.join([f'| {tabela} |' for tabela in lista_tabelas])
    output_text.delete('1.0', tk.END)  # Now this line should work fine
    output_text.insert(tk.END, tabela_formatada)

    root.mainloop()

#MOSTRA OS CONTEÚDOS DO ARQUIVO SCRIPTS_TXT
def view_scripts():
	global icon_path
	nome_arquivo = seach_script.get()
	icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
	if nome_arquivo:
		caminho_arquivo = os.path.join(diretorio_scripts, nome_arquivo)

		with open(caminho_arquivo, "r") as f:
			conteudo = f.read()

		root_script = tk.Toplevel(app, width=700, height=400)
		root_script.iconbitmap(icon_path)
		root_script.title(f"Conteúdo do Script: {nome_arquivo}")
        
		output_text_script = scrolledtext.ScrolledText(root_script, width=85, height=22, fg=c['7'])
		output_text_script.insert(tk.END, conteudo)
		output_text_script.place_configure(x=5, y=5)

		def fechar_janela():
			root_script.destroy()
        
		voltar_button_script = tk.Button(root_script, text='VOLTAR',width=10,font=st_f['f1'],background=c['6'], command=fechar_janela)
		voltar_button_script.place_configure(x=5, y=367)

# Função para salvar os dados em CSV ou PDF
def salvar_dados(headings, data):
    file_path = fd.asksaveasfilename(defaultextension=".csv", filetypes=[
                                     ("CSV Files", "*.csv"), ("PDF Files", "*.pdf")])
    if not file_path:
        return  # User cancelled save dialog

    if file_path.endswith('.csv'):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(headings)
            writer.writerows(data)

# Função para executar a consulta
def execute_query():
    global img_save_path, img_close_path
    conection = Conexao(server, database, username, password)
    query = sql_entry.get("1.0", "end-1c")
    # Caminho completo das imagens
    img_save_path = "image\\save.png"
    img_close_path = "image\\close.png"
    try:
        cursor = conection.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame.from_records(data, columns=columns)

        # Configuração da tabela
        table_data = df.values.tolist()
        table_headings = df.columns.tolist()

        # Layout com rolagem horizontal
        layout = [
            [sg.Column(
                layout=[
                    [sg.Table(values=table_data,
                               headings=table_headings,
                               display_row_numbers=False,
                               auto_size_columns=False,
                               num_rows=min(50, len(table_data)),
                               alternating_row_color=c['2'],
                               header_font=("Helvetica", 10,'bold'),
                               font=("Helvetica", 8),
                               text_color='black',
                               key='-TABLE-')]
                ],
                scrollable=True,
                vertical_scroll_only=True,
                size=(1390, 630),
                key='-COL-')
            ],
            [sg.Button(key='Salvar',image_filename=img_save_path,button_color=(sg.theme_background_color(c['3']), sg.theme_background_color(c['3'])),image_size=(50, 50), image_subsample=2, border_width=0), 
            sg.Button(key='Fechar',image_filename=img_close_path,button_color=(sg.theme_background_color(c['3']), sg.theme_background_color(c['3'])),image_size=(50, 50), image_subsample=2, border_width=0)]
        ]

        window = sg.Window('Resultado da Query',icon=icon_path, layout=layout, finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
            elif event == 'Salvar':
                # Adicione o código para salvar os dados aqui
                salvar_dados(df.columns.tolist(), df.values.tolist())

        conection.conn.close()
        window.close()
        gc.collect()  # Tentativa de liberar a memória

    except Exception as e:
        sg.popup_error(f"Erro ao executar a query: {e}")

def window_confirm():
    global bt_conf_manager,bt_conf_user, win
    win = Tk()

    win.title("Confirme!")
    win.geometry("350x150")
    win.maxsize(350,150)
    win.minsize(350,150)
    win.configure(bg=c['4'])
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    # Define as dimensões da janela
    window_width = 350
    window_height = 150
    # Calcula as coordenadas para centralizar a janela
    x = int(screen_width / 2 - window_width / 2)
    y = int(screen_height / 2 - window_height / 2)
    # Define as coordenadas da janela
    win.geometry(f"{window_width}x{window_height}+{x}+{y}")

    info_label = tk.Label(text='(Atenção!)\nSelecione um dos botões abaixo para\n alterar os dados desejados.',font=st_f['f3'],fg=c['6'],bg=c['4'])
    info_label.place_configure(x=55, y=10)

    bt_conf_user = tk.Button(text='USUÁRIO',font=('Arial',10,'bold'), width=10, border=3, borderwidth=3,command=lambda:sqllite.alter_user())
    bt_conf_user.place_configure(x=40, y=100)

    bt_conf_manager = tk.Button(text='GERENCIADOR DE LOGIN',font=('Arial',10,'bold'), border=3, borderwidth=3,command=lambda:sqllite.exclude_data4())
    bt_conf_manager.place_configure(x=150, y=100)
    win.mainloop()

def tela_termos_uso():
    global janela_termos, checkbox_var
    janela_termos = Tk()
    janela_termos.title("Termos de Uso")
    janela_termos.geometry("730x470")
    janela_termos.maxsize(730, 470)
    icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
    janela_termos.iconbitmap(icon_path)

    caminho_arquivo = "TERMOS.txt"
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            termos = arquivo.read()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de termos não encontrado.")
        exit()

    termos_text = tk.Text(janela_termos, height=400, width=100, font=("Arial", 10))
    termos_text.insert(END, termos)
    termos_text.configure(state="disabled")
    termos_text.pack(pady=10)

    # Criação da barra de rolagem
    scrollbar = Scrollbar(janela_termos, command=termos_text.xview)
    scrollbar.pack(side="right", fill="x")
    
    termos_text.config(xscrollcommand=scrollbar.set)

    janela_termos.mainloop()

def tela_sobre():
    janela_sobre= Tk()
    janela_sobre.title("História do Tech Toos")
    janela_sobre.geometry("730x470")
    janela_sobre.maxsize(730, 470)
    icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
    janela_sobre.iconbitmap(icon_path)

    caminho_arquivo = "sb.txt"
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            sobre= arquivo.read()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de sb.txt não encontrado.")
        exit()

    sobre_text = tk.Text(janela_sobre, height=400, width=100, font=("Arial", 10))
    sobre_text.insert(END, sobre)
    sobre_text.configure(state="disabled")
    sobre_text.pack(pady=10)

    # Criação da barra de rolagem
    scrollbar = Scrollbar(janela_sobre, command=sobre_text.xview)
    scrollbar.pack(side="right", fill="x")
    
    sobre_text.config(xscrollcommand=scrollbar.set)

    janela_sobre.mainloop()
    gc.collect()

def window_1():
        global app, icon_path, tree, sqllite
        app = Tk()
        app.title("Tech Tools")
        app.geometry("600x460")
        app.maxsize(600,460)
        app.minsize(600,460)
        app.configure(bg=c['3'])
        icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
        app.iconbitmap(icon_path)

        img = Img()
        execut = Execut()
        sqllite = Sqlite_Conn()
        hostname = socket.gethostname()
        version = obter_versao_atual()
        global entry_server, db_entry, user_entry, password_entry, op_dbs, check_lb_q1, check_lb_q2, check_lb_q3,seach_script,diretorio_scripts,sql_entry,check_1_var,check_2_var,check_3_var,id_entry
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()

        # Define as dimensões da janela
        window_width = 600
        window_height = 460

        # Calcula as coordenadas para centralizar a janela
        x = int(screen_width / 2 - window_width / 2)
        y = int(screen_height / 2 - window_height / 2)

        # Define as coordenadas da janela
        app.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Criando um estilo para o notebook
        style = ttk.Style()
        style.configure("TNotebook", background=c['3'])  # Define a cor de fundo do notebook
        style.map("TNotebook.Tab", background=[("background", "#104e8b")])  # Define a cor da aba selecionada


        notebook = ttk.Notebook(app, width=590, height=390,style='TNotebook')
        notebook.place_configure(x=5, y=1)
        # Criando as páginas do notebook
        page1 = tk.Frame(notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        page2 = tk.Frame(notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        page3 = tk.Frame(notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        page4 = tk.Frame(notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])

        #CRIAÇÃO DA PAGE1 E SEUS WIDGETS----------------------------------------------------------------------------------------------------------------
        notebook.add(page1, text="HOME",image=img.home)

        logo_tech = tk.Label(page1,image=img.tech,bg=c['3'],highlightbackground=c['7'])
        logo_tech.place_configure(x=120, y=70)

        frame_up = tk.Frame(page1,width=580, height=80, bg=c['3'],bd=1,highlightthickness=1,highlightbackground=c['2'])
        frame_up.place_configure(x=2, y=5)

        def terms(event):
            tela_termos_uso()

        termos_label = tk.Label(app, text='Termos de Uso  |', font=st_f['f2'], bg=c['3'], fg=c['2'])
        termos_label.place_configure(x=140, y=440)
        termos_label.bind("<Button-1>",terms)

        def arq_sobre(event):
            tela_sobre()
        sobre_label = tk.Label(app,text='Sobre...',font=st_f['f2'],bg=c['3'],fg=c['2'])
        sobre_label.place_configure(x=240, y=440)
        sobre_label.bind("<Button-1>",arq_sobre)

        version_label = tk.Label(app,text=f'Tech Tools ®  -  v{version}  |',font=st_f['f2'], bg=c['3'], fg=c['2'])	
        version_label.place_configure(x=5, y=440)

        list_servers = tk.Label(app,text=f"Servers DB's Ativos:  {lists_servers()} ",font=('Helvetica',7,'bold'),fg=c['2'],bg=c['3'],foreground=c['2'])
        list_servers.place_configure(x=170, y=20)

        #FIM -----------------------------------------------------------------------------------------------------------------------------------------


        #BOTÕES SUPERIORES ----------------------------------------------------------------------------------------------
        notebook.add(page2, text="CONEXÕES DB",image=img.mundo)
        bt_ibexpert = tk.Button(page2, image=img.ibexpert,bg=c['2'], command= lambda:execut.ibexpert())
        bt_ibexpert.place_configure(x=503, y=90)

        #FRAME MEIO---------------------------------------------------------------------------------------------------

        label_server = tk.Label(page2, text='Servidor:',font=st_f['f4'], bg=c['3'], fg=c['2'])
        label_server.place_configure(x=5, y=28)

        label_exemp = tk.Label(page2, text='Ex: "Nome_computador\Instância"',font=st_f['f2'], bg=c['3'], fg=c['2'])
        label_exemp.place_configure(x=100, y=28)

        entry_server = tk.Entry(page2,font=st_f['f3'],width=47,bd=2,highlightthickness=1,highlightbackground=c['7'] ,fg=c['6'])
        entry_server.place_configure(x=5, y=57)
        entry_server.insert(tk.END, f"{hostname}\\")


        op_dbs = ttk.Combobox(page2, values=['MySQL','SQL Server'],font=st_f['f3'],foreground=c['6'], width=10)
        op_dbs.place_configure(x=348, y=57)
 


        bt_conect = tk.Button(page2,text='CONECTAR',width=10,fg=c['2'],bg=c['5'], command=lambda:conectar())
        bt_conect.place_configure(x=480,y=54)
        

        db_label = tk.Label(page2,text='DATA BASE',font=st_f['f2'],bg=c['3'],fg=c['2'])
        db_label.place_configure(x=7, y=90)
        db_entry = tk.Entry(page2, width=13,bd=2,highlightthickness=1,highlightbackground=c['7'],fg=c['6'],font=st_f['f3'])
        db_entry.place_configure(x=5, y=110)

        user_label = tk.Label(page2,text='LOGON',font=st_f['f2'],bg=c['3'],fg=c['2'])
        user_label.place_configure(x=126, y=90)
        user_entry = tk.Entry(page2,width=13,bd=2,highlightthickness=1,highlightbackground=c['7'],fg=c['6'],font=st_f['f3'])
        user_entry.place_configure(x=125, y=110)

        password_label = tk.Label(page2,text='SENHA',font=st_f['f2'],bg=c['3'],fg=c['2'])
        password_label.place_configure(x=241, y=90)
        password_entry = tk.Entry(page2,width=13,font=st_f['f3'],bd=2,highlightthickness=1,highlightbackground=c['7'],fg=c['6'])
        password_entry.place_configure(x=240, y=110)

        check_label = tk.Label(page2,text='Autenticação\ndo Windows',font=st_f['f6'],bg=c['3'],fg=c['1'])
        check_label.place_configure(x=370, y=100)
        check = tk.Checkbutton(page2, width=1,bg=c['3'],fg=c['1'])
        check.place_configure(x=336, y=112)

        #Linha que separa o frame no meio ----------------------------------------------------------------------------------------------
        linha1 = tk.Canvas(page2, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha1.place_configure(x=2, y=148)

        info_label = tk.Label(page2, text='Escolha a tabela que deseja baixar:',font=st_f['f2'], bg=c['3'], fg=c['2'])
        info_label.place_configure(x=5, y=160)

        check_1_var = tk.IntVar()
        check_lb_q1 = tk.Label(page2,text='CLIENTES',font=st_f['f6'],bg=c['3'],fg=c['1'])
        check_lb_q1.place_configure(x=35, y=185)
        check_q1 = tk.Checkbutton(page2, width=1,bg=c['3'],fg=c['1'], variable=check_1_var)
        check_q1.place_configure(x=2, y=182)

        check_2_var = tk.IntVar()
        check_lb_q2 = tk.Label(page2,text='FORNECEDORES',font=st_f['f6'],bg=c['3'],fg=c['1'])
        check_lb_q2.place_configure(x=165, y=185)
        check_q2 = tk.Checkbutton(page2, width=1,bg=c['3'],fg=c['1'],variable=check_2_var)
        check_q2.place_configure(x=130, y=182)

        check_3_var = tk.IntVar()
        check_lb_q3 = tk.Label(page2,text='PRODUTOS',font=st_f['f6'],bg=c['3'],fg=c['1'])
        check_lb_q3.place_configure(x=335, y=185)
        check_q3 = tk.Checkbutton(page2, width=1,bg=c['3'],fg=c['1'],variable=check_3_var)
        check_q3.place_configure(x=300, y=182)

        bt_baixar = tk.Button(page2,text='BAIXAR',width=8,fg=c['2'],bg=c['5'], command=lambda:seach_sql())
        bt_baixar.place_configure(x=480,y=182)

        linha2 = tk.Canvas(page2, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha2.place_configure(x=2, y=220)

        label_info2 = tk.Label(page2, text='CONSULTA SQL:',font=st_f['f6'], bg=c['3'], fg=c['2'])
        label_info2.place_configure(x=2, y=225)

        sql_entry = tk.Text(page2,width=71,height=4,bd=1,highlightthickness=1,highlightbackground=c['7'])
        sql_entry.place_configure(x=2, y=250)

        query = tk.Button(page2,text='EXECUTAR',width=10,fg=c['2'],bg=c['5'], command=lambda:execute_query())
        query.place_configure(x=2,y=325)

        most_tables = tk.Button(page2,text='MOSTRAR TABELAS',width=15,fg=c['2'],bg=c['5'], command=lambda:view_tables())
        most_tables.place_configure(x=100,y=325)
        
        #FIM PAGE2------------------------------------------------------------------------------------------------------------

        
        notebook.add(page3, text="UTILITARIOS", image=img.ultili)
        script_label = tk.Label(page3, text='Buscar Scripts:',font=st_f['f4'],fg=c['2'],bg=c['3'])
        script_label.place_configure(x=5, y=5)

        diretorio_scripts = os.path.join(os.path.dirname(__file__), 'scripts_txt')

        # Listar os arquivos .txt no diretório
        arquivos_txt = [arquivo for arquivo in os.listdir(
            diretorio_scripts) if arquivo.endswith('.txt')]

        seach_script = ttk.Combobox(page3, values=arquivos_txt, width=50, height=30)
        seach_script.place_configure(x=5, y=30)

        bt_script = tk.Button(page3, text='MOSTRAR SCRIPT',height=-20, command=lambda:view_scripts())
        bt_script.place_configure(x=350, y=30)

        linha3 = tk.Canvas(page3, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha3.place_configure(x=2, y=65)

        global aq_inst, bt_baixar_file, bt_baixar_print, prints
        aq_inst_label = tk.Label(page3,text='Arquivos de Instalação:',font=st_f['f4'],fg=c['2'],bg=c['3'])
        aq_inst_label.place_configure(x=5, y=80)
        aq_inst = ttk.Combobox(page3, values=arquivos, width=50, height=30)
        aq_inst.place_configure(x=5, y=110)
        
        bt_baixar_file = tk.Button(page3,text='BAIXAR',width=10, height=-20,command=lambda:file_list())
        bt_baixar_file.place_configure(x=350, y=110)

        linha4 = tk.Canvas(page3, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha4.place_configure(x=2, y=150)

        print_label = tk.Label(page3,text='Drivers Impressoras:',font=st_f['f4'],fg=c['2'],bg=c['3'])
        print_label.place_configure(x=5, y=160)
        prints = ttk.Combobox(page3, values=impres, width=50, height=30)
        prints.place_configure(x=5, y=190)
        
        bt_baixar_print = tk.Button(page3,text='BAIXAR',width=10, height=-20,command=lambda:list_printers())
        bt_baixar_print.place_configure(x=350, y=190)
        
        
        #CRIAÇÃO DA PAGE4 E SEUS WIDGETS----------------------------------------------------------------------------------------------------------------
        notebook.add(page4, text='Usuários',image=img.users)
        linha5 = tk.Canvas(page4, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha5.place_configure(x=2, y=45)
        global manager_pass_et,manager_user_et, email_entry, obs_entry, bt_save_dados, new_user_var, alt_user_var
        title4 = tk.Label(page4, text='GERENCIADOR DE SENHAS E USUÁRIOS',font=st_f['f3'], bg=c['3'], fg=c['2'])
        title4.place_configure(x=150, y=10)

        manager_user_lb = tk.Label(page4, text="Nome:",font=st_f['f3'], bg=c['3'], fg=c['2'])
        manager_user_lb.place_configure(x=5, y=60)

        manager_user_et = tk.Entry(page4, width=25, bd=1,highlightthickness=1,highlightbackground=c['7'])
        manager_user_et.place_configure(x=65, y=60)

        manager_pass_lb = tk.Label(page4, text="Senha:",font=st_f['f3'], bg=c['3'], fg=c['2'])
        manager_pass_lb.place_configure(x=5, y=100)

        manager_pass_et = tk.Entry(page4, width=25, bd=1,highlightthickness=1,highlightbackground=c['7'], show="*")
        manager_pass_et.place_configure(x=65, y=100)

        email_label = tk.Label(page4, text="E-mail:",font=st_f['f3'], bg=c['3'], fg=c['2'])
        email_label.place_configure(x=230 , y=60)

        email_entry = tk.Entry(page4, width=45, bd=1,highlightthickness=1,highlightbackground=c['7'])
        email_entry.place_configure(x=280, y=60)

        obs_label = tk.Label(page4, text="Obs:",font=st_f['f3'], bg=c['3'], fg=c['2'])
        obs_label.place_configure(x=230 , y=100)

        obs_entry = tk.Entry(page4, width=45, bd=1,highlightthickness=1,highlightbackground=c['7'])
        obs_entry.place_configure(x=280, y=100)
        
        new_user_var = tk.IntVar()
        alt_user_var = tk.IntVar()
        new_user_label = tk.Label(page4, text="Novo Usuário",font=st_f['f2'], bg=c['3'], fg=c['2'])
        new_user_label.place_configure(x=30 , y=138)

        new_user_entry = tk.Checkbutton(page4,bg=c['3'],fg=c['1'],variable=new_user_var)
        new_user_entry.place_configure(x=5, y=137)


        alt_user_label = tk.Label(page4, text="GERENCIADOR DE LOGIN",font=st_f['f2'], bg=c['3'], fg=c['2'])
        alt_user_label.place_configure(x=150 , y=138)

        alt_user_entry = tk.Checkbutton(page4,bg=c['3'],fg=c['1'],variable=alt_user_var)
        alt_user_entry.place_configure(x=120, y=137)
        

        id_label = tk.Label(page4, text='Id:',font=st_f['f3'], bg=c['3'], fg=c['2'])
        id_label.place_configure(x=5, y=179)

        id_entry = tk.Entry(page4, width=10, bd=1,highlightthickness=1,highlightbackground=c['7'])
        id_entry.place_configure(x=30, y=178)

        bt_alterar = tk.Button(page4,text='ALTERAR', width=10,fg=c['2'],bg=c['1'], command=lambda:sqllite.alter_user())#--------------------------------------------------------------------------
        bt_alterar.place_configure(x=310, y=172)

        bt_excluir = tk.Button(page4,text='EXCLUÍR', width=10,fg=c['2'],bg=c['6'], command=lambda:sqllite.exclude_data4())#--------------------------------------------------------------------------
        bt_excluir.place_configure(x=395, y=172)

        bt_excluir = tk.Button(page4,text='SALVAR', width=10,fg=c['2'],bg=c['5'], command=lambda:sqllite.add_manager_pass())#--------------------------------------------------------------------------
        bt_excluir.place_configure(x=479, y=172)
        #LINHA 6 ---------------------------------------------------------------------------------------------------------------
        linha6 = tk.Canvas(page4, width=570, height=0,bd=1,highlightthickness=1,highlightbackground=c['7'])
        linha6.place_configure(x=2, y=200)
        
        global seach_dados,bt_seach_dados
        seach_dados_label = tk.Label(page4, text='Pesquisar:', font=st_f['f3'],bg=c['3'], fg=c['2'])
        seach_dados_label.place_configure(x=5, y=210)

        seach_info_label = tk.Label(page4, text='( nome,email )', font=st_f['f5'],bg=c['3'], fg=c['2'])
        seach_info_label.place_configure(x=76, y=215)

        seach_dados = tk.Entry(page4,width=45, bd=1,highlightthickness=1,highlightbackground=c['7'])
        seach_dados.place_configure(x=5, y=230)

        bt_seach_dados = tk.Button(page4,text='PESQUISAR', width=12,fg=c['2'],bg=c['5'],command=lambda:sqllite.seach_data_page4())
        bt_seach_dados.place_configure(x=290,y=230)


        # Criação da Treeview (vazia inicialmente)
        tree = ttk.Treeview(page4, height=5, selectmode='browse', 
        columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'], show='headings')
        tree.place_configure(x=5, y=265)

        tree.column('Column1', width=20, anchor=CENTER, stretch=tk.NO)
        tree.heading('#1', text='ID')
        tree.column('Column2', width=200,anchor=CENTER, minwidth=50, stretch=NO)
        tree.heading('#2', text='Nome')
        tree.column('Column3', width=100,anchor=CENTER, minwidth=50, stretch=NO)
        tree.heading('#3', text='Senha')
        tree.column('Column4', width=100, minwidth=50, stretch=NO)
        tree.heading('#4', text='Email.')
        tree.column('Column5', width=170, minwidth=50, stretch=NO)
        tree.heading('#5', text='Obs.')
        
        
        tree.tag_configure("gray", background='lightgray')
        tree.tag_configure("normal", background='white')
  
        for rows in sqllite.result:
            tree.insert("", "end",iid=rows[0],text=[0], values=rows)
    
        app.mainloop()
        gc.collect()

window_1()