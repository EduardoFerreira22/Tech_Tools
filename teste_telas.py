from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox, filedialog, scrolledtext
import tkinter as tk
from functions import Widgets,Funcoes
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import pandas as pd
import PySimpleGUI as sg
import sqlite3
import pycipher
import psutil
import socket
import pyodbc
import mysql.connector
import webbrowser
import datetime
import bcrypt
import csv
import os
import re
import gc
#IMPORTANDO AS FUNÇÕES DO ARQUIVO EXECUT.PY

#DICIONÁRIO DE FONTES USADAS DENTRO DO PROGRAMA.
st_f = {'f1':('M Hei PRC', 10, 'bold'),'f2':('Helvetica', 8,'bold','italic'),'f3':('Helvetica', 10, 'bold'),'f4':("Helvetica", 12, "bold"),'f5':('Helvetica', 7, 'italic'),'f6':('New', 9,'bold'),'f7':('Arial', 10, 'bold')}

#DICIONÁRIO DE CORES USADAS DENTRO DO PROGRAMA.
# C REPRESENTA CORES
		#CORES	LARANJA			BRANCO		 AZUL ESCURO	AZUL CEU	  VERDE			VERMELHO
c: dict = {'1':'#e69138', '2':'#ffffff','3':'#033364', '4':'#f0ffff','5':'#44ab4c','6':'#e32636','7':'#000000'}


# Query's que serão responsáveis pelas consultas no banco de dados
#NÃO  CONSEGUI TER ACESSO A ESSAS QUERYS A PARTIR DE OUTRO ARQUIVO


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
            desired_size5 = (590, 390)  # Tamanho desejado
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
class Func:

    def abrir_tela_app(self,login):
        # Declarar a variável login como global
        login.destroy()
        self.win_config()

    def show_progress_bar(self,login):
        
        progress_bar = ttk.Progressbar(login, mode='determinate', maximum=100, length=400)  # Altere o valor de 'length' conforme necessário
        progress_bar.place(x=230, y=520)
        progress_bar.start(1)  # Inicia a animação do ProgressBar
        increment = 1  # Valor do incremento a cada iteração
        total_iterations = 1  # Total de iterações para atingir 100%
        update_interval = 5000000 / total_iterations  # Tempo entre cada iteração (em milissegundos)

        def update_progress():
            nonlocal increment
            current_value = progress_bar['value'] + increment
            if current_value <= 10:
                progress_bar['value'] = current_value
                login.after(int(update_interval), update_progress)  # Ajuste o tempo aqui (em milissegundos)
            else:
                progress_bar.stop()  # Para a animação do ProgressBar
                progress_bar.destroy()  # Remove o ProgressBar da tela
                self.abrir_tela_app()

        login.after(int(update_interval), update_progress)  # Ajuste o tempo aqui (em milissegundos)

    def verificar_login(self,login):
        login_conn = Sqlite_Conn()
        user = self.user_login_et.get()
        password = self.pass_login_et.get()

        # Consulta para recuperar os dados do usuário com base no nome de usuário
        comando_users = "SELECT USER, PASSWORD FROM USERS WHERE USER = ?"
        user_data = (user,)  # Usando um parâmetro de ligação

        login_conn.cursor.execute(comando_users, user_data)
        stored_user_data = login_conn.cursor.fetchone()

        if stored_user_data:
            stored_password_hash = stored_user_data[1]
            # Verifique se a senha fornecida corresponde ao hash armazenado
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                # A senha está correta, continue com o login
                # Recupere o tipo de acesso do usuário
                tipo_acesso_query = "SELECT USER,TYPE_US FROM USERS WHERE USER = ?"
                login_conn.cursor.execute(tipo_acesso_query, user_data)
                tipo_acesso = login_conn.cursor.fetchone()

                if tipo_acesso:
                    print(f"Tipo de acesso do usuário {user}: {tipo_acesso[1]}")
                else:
                    print(f"Tipo de acesso não encontrado para o usuário {user}")

                self.show_progress_bar(login)
                login.after(100, lambda: self.abrir_tela_app(login))
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado")

        login_conn.cursor.close()


class Aplication(Func,Widgets,Funcoes):
    def __init__(self):
        # Chame o construtor das classes pai
        super().__init__()
        self.root = self.create_tela(titulo='Tech Tools',geometria='600x460',resizable=(False,False),bg=c['3'],w_width=600,w_height=460)
        self.create_notebooks()
        self.page_1()
        self.page_2()
        self.page_3()
        self.page_4()
        self.run()

    def run(self):
        self.root.mainloop()

    def create_notebooks(self):
        # Criando um estilo para o notebook
        style = ttk.Style()
        style.configure("TNotebook", background=c['3'])  # Define a cor de fundo do notebook
        style.map("TNotebook.Tab", background=[("background", "#104e8b")])  # Define a cor da aba selecionada
        self.notebook = self.func_notebooks(master=self.root,width=590,height=390,style='TNotebook',x=5,y=1)

        # Criando as páginas do notebook
        self.page1 = tk.Frame(self.notebook,bg=c['7'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        self.page2 = tk.Frame(self.notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        self.page3 = tk.Frame(self.notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])
        self.page4 = tk.Frame(self.notebook,bg=c['3'],bd=1,highlightthickness=2,highlightbackground=c['7'])

    #cria a primeira tela e seus objetos
    def page_1(self):
        self.img = Img()
        self.notebook.add(self.page1, text="HOME",image=self.img.home)

        self.logo_tech = self.labels(master=self.page1,text='',image=self.img.tech,bg=c['3'],x=0,y=0,highlightbackground=c['7'])

        def func_terms(self,event):
             'tela_termos_uso()'

        self.termos_label = self.labels(master=self.root,text='Termos de Uso  |',x=140,y=440,font=st_f['f2'], bg=c['3'], fg=c['2'])
        self.termos_label.bind("<Button-1>",func_terms)
        
        def arq_sobre(self,event):
            'tela_sobre()'
        sobre_label = self.labels(master=self.root,text='Sobre...',x=240, y=440,font=st_f['f2'],bg=c['3'],fg=c['2'])
        sobre_label.bind("<Button-1>",arq_sobre)

        self.user_label = self.labels(master=self.root,text=f'teste',x=300, y=440,font=st_f['f2'],bg=c['3'],fg=c['2'])

        self.version_label = self.labels(master=self.root,text=f'Tech Tools ®  -  vversion  |',x=5, y=440,font=st_f['f2'], bg=c['3'], fg=c['2'])	

        self.list_servers = self.labels(master=self.root,text=f"Servers DB's Ativos:  {self.lists_servers()} ",x=170, y=20,font=('Helvetica',7,'bold'),fg=c['2'],bg=c['3'],foreground=c['2'])

    #cria a segunda  tela e seus objetos (tela de conexões data bases)
    def page_2(self):
        self.notebook.add(self.page2, text="CONEXÕES DB",image=self.img.mundo)
        pass

    #cria a terceira tela e seus objetos (Arquivos de intalação e outros)
    def page_3(self):
        self.notebook.add(self.page3, text="UTILITARIOS", image=self.img.ultili)
        pass
    #Cria a quarta tela e seus objetos  (gerenciamento de logins e senhas)
    def page_4(self):
        self.notebook.add(self.page4, text='Usuários',image=self.img.users)
        pass


if __name__=='__main__':
    Aplication()