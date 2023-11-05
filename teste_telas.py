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
#IMPORTANDO AS FUNÇÕES DO ARQUIVO EXECUT.PY
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

app = Tk()
class Aplication():
  def __init__(self):
    self.app = app
    self.win_config()
    app.mainloop()

  def win_config(self):
      self.app.title("Tech Tools")
      self.app.geometry("600x460")
      self.app.maxsize(600,460)
      self.app.minsize(600,460)
      # self.app.configure(bg=c['3'])
      icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
      self.app.iconbitmap(icon_path)

      #instâncias de classes
      # img = Img()
      # execut = Execut()
      # sqllite = Sqlite_Conn()
      # hostname = socket.gethostname()
      # version = obter_versao_atual()
      screen_width = self.app.winfo_screenwidth()
      screen_height = self.app.winfo_screenheight()
      # Define as dimensões da janela
      window_width = 600
      window_height = 460
      # Calcula as coordenadas para centralizar a janela
      x = int(screen_width / 2 - window_width / 2)
      y = int(screen_height / 2 - window_height / 2)
      # Define as coordenadas da janela
      self.app.geometry(f"{window_width}x{window_height}+{x}+{y}")

  def widgets_frame_1(self):
     pass
  


if __name__=='__main__':
  Aplication()
