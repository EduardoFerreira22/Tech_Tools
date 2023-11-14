import tkinter as tk
from tkinter import ttk
from tkinter import *
import psutil
import os
import re

class Widgets():

    def labels(self, master, text, x, y, **kwargs):
        self.label_config = tk.Label(master=master, text=text,**kwargs)
        self.label_config.place_configure(x=x, y=y)
        return self.label_config

    def buttons(self, master,text, width, height, x, y, **kargs):
        self.bt_config = tk.Button(master=master,text=text, width=width, height=height)
        self.bt_config.place_configure(x=x, y=y)

    def entrys(self, master, width, height, x, y, **kargs):
        self.ent_config = tk.Entry(master=master, width=width, height=height)
        self.ent_config.place_configure(x=x, y=y)

    def frames(self, master, width, height, x, y, **kargs):
        self.frm_config = tk.Frame(master=master, width=width, height=height)
        self.frm_config.place_configure(x=x, y=y)

    def check_buttons(self, master, border, fg, x, y, **kargs):
        self.check_bt_config = tk.Checkbutton(master=master, border=border, fg=fg)
        self.check_bt_config.place_configure(x=x, y=y)

    def create_tela(self,titulo, geometria, resizable, bg, w_width, w_height):
        self.tela = Tk()
        self.tela.title(titulo)
        self.tela.geometry(geometria)
        self.tela.resizable(*resizable)  # Use o operador * para desempacotar a tupla
        self.tela.configure(bg=bg)
        icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
        self.tela.iconbitmap(icon_path)
        screen_width = self.tela.winfo_screenwidth()
        screen_height = self.tela.winfo_screenheight()

        # Define as dimensões da janela
        w_width = w_width
        w_height = w_height

        # Calcula as coordenadas para centralizar a janela
        x = int(screen_width / 2 - w_width / 2)
        y = int(screen_height / 2 - w_height / 2)

        # Define as coordenadas da janela
        self.tela.geometry(f"{w_width}x{w_height}+{x}+{y}")
        return self.tela

    def func_notebooks(self,master,width,height,style,x,y):
        self.f_notebook = ttk.Notebook(master=master, width=width,height=height,style=style)
        self.f_notebook.place_configure(x=x,y=y)
        return self.f_notebook

        
class Funcoes():
    #REALIZA A BUSCA POR SERVIDORES DE BANCO DE DADOS ATIVOS NO MOMENTO.
    def lists_servers(self):
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