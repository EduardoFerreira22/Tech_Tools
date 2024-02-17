from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)
from ui_process_csv import Ui_ProcessCSV
import sys
import os
import csv



#A classe abaixo está herdando tudo das classes QMainWindow do Pyside6 e Ui_MainWindow que é a classe que contém a tela criada no QtDesigner
class Processing_CSV(QMainWindow,Ui_ProcessCSV):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Processamento de planilhas.")
        appIcon = QIcon(u"img\\TECH NEW LOGO.png")
        self.setWindowIcon(appIcon)

    #######################  BOTÕES  ##############################################################################
        self.bt_buscar_filecsv.clicked.connect(self.buscar_arquivo)
        self.bt_processar_arquivo_csv.clicked.connect(self.processar_csv)


    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def buscar_arquivo(self):
        #Abre um diálogo de seleção de arquivos
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Arquivo CSV UTF-8 (*.csv);;CSV separado por vírgula (*.csv)")

        if file_dialog.exec():
            #Obtém o caminho do arquivo selecionado
            selected_file = file_dialog.selectedFiles()[0]

            #Define o caminho do arquivo dentro do QLineEdit
            self.txt_path_filecsv.setText(selected_file)

    def processar_csv(self):
        path_csv = self.txt_path_filecsv.text()

        if path_csv == '':
            self.txt_output_logs.appendPlainText("Erro: Usuário tentou processar, sem ter selecionado um arquivo antes.")
            self.show_error_popup("Atenção!", "Não é possível processar antes do usuário selecionar o arquivo.csv")
        else:
            self.txt_output_logs.appendPlainText("\nIniciando leitura...")
            self.txt_output_logs.appendPlainText(f"\nProcessando arquivo CSV: {path_csv}")

            # Abre o arquivo e lê
            with open(path_csv, 'r', newline='') as file_csv:
                csv_reader = csv.reader(file_csv, delimiter=';')  # Especifica o delimitador como ponto e vírgula
                
                # Lê o cabeçalho para obter os nomes das colunas
                header = next(csv_reader)
                num_cols = len(header)
                
                # Define o número de linhas na tabela
                num_rows = sum(1 for _ in csv_reader)  # Conta as linhas restantes no arquivo CSV
                file_csv.seek(0)  # Volta para o início do arquivo para ler novamente
                
                self.tb_dados_csv.setRowCount(num_rows)
                self.tb_dados_csv.setColumnCount(num_cols)
                
                # Define os cabeçalhos da tabela
                self.tb_dados_csv.setHorizontalHeaderLabels(header)
                
                # Lê os dados e preenche a tabela, começando da linha 2 para evitar a repetição dos cabeçalhos
                for row_idx, row_data in enumerate(csv_reader):
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(cell_data)
                        self.tb_dados_csv.setItem(row_idx - 1, col_idx, item)  # Adiciona 1 ao índice de linha para começar da linha 2
                self.txt_output_logs.appendPlainText("\nDados do arquivo CSV inseridos na tabela com sucesso.")
        
                self.insert_heads_comboBox(header)       
                            
    def insert_heads_comboBox(self,head):
        for h in head:
            colum_names = h
            print(colum_names)



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Processing_CSV()
    window.show()
    sys.exit(app.exec())

