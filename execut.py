from tkinter import  messagebox
import subprocess
import webbrowser
import psutil
import os


icon_path = os.path.join(os.path.dirname(__file__), 'image', 'IMG.ico')
#EXECUTA O ARQUIVO .EXE DO IBEXPERT NA PASTA IBExpert
def ib_expert():
	ibexpert_process = None
	resp = messagebox.askyesno("Confirmação!", "Deseja executar o IBExpert?")
	if resp:
		# pega o caminho do arquivo em qualquer outra máquina
		nome_arquivo = os.path.join(os.path.dirname(
                    __file__), 'resources', 'ibexpert.exe')

				# não permite que a execução do arquivo se torne um loop
		if ibexpert_process is None or not psutil.pid_exists(ibexpert_process.pid):
			ibexpert_process = subprocess.Popen(nome_arquivo)
		else:
			messagebox.showinfo("Atenção!",'IBExpert já está em execução!',icon=icon_path)

def exec_rufus():
    rufus_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Rufus?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        verificador_rufus = os.path.join(
            os.path.dirname(__file__), 'resources', 'rufus.exe')

            # não permite que a execução do arquivo se torne um loop
        if rufus_process is None or not psutil.pid_exists(rufus_process.pid):
                        rufus_process = subprocess.Popen(verificador_rufus)
        else:
            messagebox.showinfo("Atenção!",'Rufus já está em execução!',icon=icon_path)

def exe_anydesk():
    anydesk_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o AnyDesk?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        verificador_anydesk = os.path.join(
            os.path.dirname(__file__), 'resources', 'AnyDesk.exe')

        # não permite que a execução do arquivo se torne um loop
        if anydesk_process is None or not psutil.pid_exists(anydesk_process.pid):
                        anydesk_process = subprocess.Popen(verificador_anydesk)
        else:
            messagebox.showinfo("Atenção!",'Any Desk já está em execução!',icon=icon_path)

#ATIVADORES -----------------------------------------------------------------------------------------
def exec_reloader():
    reloader_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Reloader?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        verificador_reloader = os.path.join(
            os.path.dirname(__file__), 'resources', 'RELOAD.exe')

                # não permite que a execução do arquivo se torne um loop
        if reloader_process is None or not psutil.pid_exists(reloader_process.pid):
                    reloader_process = subprocess.Popen(verificador_reloader)
        else:
            messagebox.showinfo("Atenção!",'Reloader já está em execução!',icon=icon_path)

def exec_win11():
    win11_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Ativador do Win 11?")
    if resp:
        ativador_win11 = os.path.join(
            os.path.dirname(__file__), 'resources', 'win11.cmd')

        # não permite que a execução do arquivo se torne um loop
        if win11_process is None or not psutil.pid_exists(win11_process.pid):
                    win11_process = subprocess.Popen(ativador_win11)
        else:
            messagebox.showinfo("Atenção!",'Ativador Windows 11 já está em execução!',icon=icon_path)

def exec_office21():
    office_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Ativador Office 2021?")
    if resp:
        ativador_winoffice = os.path.join(os.path.dirname(
            __file__), 'resources', 'office2021.cmd')

            # não permite que a execução do arquivo se torne um loop
        if office_process is None or not psutil.pid_exists(office_process.pid):
                office_process = subprocess.Popen(ativador_winoffice)
        else:
            messagebox.showinfo("Atenção!",'Ativador Office 2021 já está em execução!',icon=icon_path)

def exec_driver_rede():
    driversrede_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o 3DP Drivers de Rede?")
    if resp:
        driver_rede = os.path.join(os.path.dirname(
            __file__), 'resources', '3DP.exe')

        # não permite que a execução do arquivo se torne um loop
        if driversrede_process is None or not psutil.pid_exists(driversrede_process.pid):
            driversrede_process = subprocess.Popen(driver_rede)
        else:
            messagebox.showinfo("Atenção!",'3DP já está em execução!',icon=icon_path)

def exec_p_hiper():
    hiper_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Preparador de ambiente Hiper?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        arquivo_hiper = os.path.join(os.path.dirname(
            __file__), 'resources', 'Hiper.bat')

        # não permite que a execução do arquivo se torne um loop
        if hiper_process is None or not psutil.pid_exists(hiper_process.pid):
            hiper_process = subprocess.Popen(arquivo_hiper)
        else:
            messagebox.showinfo("Atenção!",'Pré-Implantação Hiper já está em execução!',icon=icon_path)

def exec_cristal_disk():
    cristal_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Crystal Disk Info?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        arquivo_cristal = os.path.join(os.path.dirname(
            __file__), 'resources', 'CrystalDiskInfo.exe')

        # não permite que a execução do arquivo se torne um loop
        if cristal_process is None or not psutil.pid_exists(cristal_process.pid):
            cristal_process = subprocess.Popen(arquivo_cristal)
        else:
            messagebox.showinfo("Atenção!",'CrystalDiskInfo já está em execução!',icon=icon_path)

def exec_wintohdd():
    hdd_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o WinToHDD?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        arquivo_wintohdd = os.path.join(os.path.dirname(
            __file__), 'resources', 'WinToHDD_Free.exe')

        # não permite que a execução do arquivo se torne um loop
        if hdd_process is None or not psutil.pid_exists(hdd_process.pid):
            hdd_process = subprocess.Popen(arquivo_wintohdd)
        else:
            messagebox.showinfo("Atenção!",'WinToHDD_Free já está em execução!',icon=icon_path)

def exec_ipscaner():
    ipscaner_process = None
    resp = messagebox.askyesno("Confirmação!", "Deseja executar o Advanced_IP_Scanner?")
    if resp:
        # pega o caminho do arquivo em qualquer outra máquina
        arquivo_ipscaner = os.path.join(os.path.dirname(
            __file__), 'resources', 'Advanced_IP_Scanner.exe')

        # não permite que a execução do arquivo se torne um loop
        if ipscaner_process is None or not psutil.pid_exists(ipscaner_process.pid):
            ipscaner_process = subprocess.Popen(arquivo_ipscaner)
        else:
            messagebox.showinfo("Atenção!",'Advanced_IP_Scanner já está em execução!',icon=icon_path)

def setup_hiper():
    webbrowser.open('https://downloads.hiper.com.br/Hiper.Setup.exe')
def e_trade1():
    webbrowser.open('https://vrsystem.info/files/Install_ETrade.exe')
def e_trade2():
    webbrowser.open('https://vrsystem.info/files/Stable_ETrade.exe')


