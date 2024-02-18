from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)
from ui_process_csv import Ui_ProcessCSV
from datetime import datetime
from collections import defaultdict
import sys
import csv
import json
import os


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
        self.bt_buscar_opcoes.clicked.connect(self.combo_op_busca)

        #PROCESSAMENTO
        self.comboBox_op_processamentos.currentIndexChanged.connect(self.combo_op_processamento)
        self.bt_executar_process.clicked.connect(self.exetuc_process)
        self.txt_alt_NCM1.setVisible(False)
        self.txt_alt_NCM2.setVisible(False)
        self.bt_setas_ncm.setVisible(False)


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
        self.path_csv = self.txt_path_filecsv.text()

        if self.path_csv == '':
            self.txt_output_logs.appendPlainText("Erro: Usuário tentou processar, sem ter selecionado um arquivo antes.")
            self.show_error_popup("Atenção!", "Não é possível processar antes do usuário selecionar o arquivo.csv")
        else:
            self.txt_output_logs.appendPlainText("\nIniciando leitura...")
            self.txt_output_logs.appendPlainText(f"\nProcessando arquivo CSV: {self.path_csv}")

            # Abre o arquivo e lê
            with open(self.path_csv, 'r', newline='') as file_csv:
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
        
 
    def processing_ncms_json(self):
        try:
            with open('resource\\EXPIRED_NCM.json', 'r', encoding='utf-8') as f:
                expired_ncms_data = json.load(f)
                expired_ncms = [ncm['Codigo'] for ncm in expired_ncms_data.get('Nomenclaturas', [])]
                return expired_ncms
        except FileNotFoundError:
            self.show_error_popup("Erro!", "Arquivo 'EXPIRED_NCM.json' não encontrado.")

    def processing_ncm_csv(self):
        try:
            with open(self.path_csv, 'r') as file_csv:
                csv_reader = csv.reader(file_csv, delimiter=';')
                csv_data = [row for row in csv_reader]  # Lê todos os dados do CSV
                return csv_data
        except Exception as e:
            self.show_error_popup("Erro!", "Arquivo csv não encontrado.")
    
    def combo_op_busca(self):
        opcoes = self.comboBox_op_busca.currentText()
        self.txt_output_logs.appendPlainText(f"\nOpção selecionada: {opcoes}")
        if opcoes == '':
            self.show_error_popup("Erro!", f"É necessário selecionar uma das opções antes de realizar a busca.")
            self.txt_output_logs.appendPlainText(f"Erro: Nenhuma opção de busca selecionada.")
        else:
            pass

        if opcoes == 'Buscar por NCM':
            self.search_by_ncm()
        elif opcoes == "Buscar NCM's inválidos.":
            self.search_invalid_ncm()

    def combo_op_processamento(self):
        opcoes = self.comboBox_op_processamentos.currentText()
        self.txt_output_logs.appendPlainText(f"Opção selecionada: {opcoes}")

        if opcoes == '':
            self.show_error_popup("Erro!", f"É necessário selecionar uma das opções antes de realizar a busca.")
            self.txt_output_logs.appendPlainText(f"Erro: Nenhuma opção de busca selecionada.")
        else:
            pass

        if opcoes == 'Substituir NCM.':
            self.txt_alt_NCM1.setVisible(True)
            self.txt_alt_NCM2.setVisible(True)
            self.bt_setas_ncm.setVisible(True)
            ncm1 = self.txt_alt_NCM1.text()
            ncm2 = self.txt_alt_NCM2.text()
            self.update_ncm(ncm1,ncm2)

    def exetuc_process(self):
        opcoes = self.comboBox_op_processamentos.currentText()
        self.txt_output_logs.appendPlainText(f"Opção selecionada: {opcoes}")

        if opcoes == '':
            self.show_error_popup("Erro!", f"É necessário selecionar uma das opções antes de realizar a busca.")
            self.txt_output_logs.appendPlainText(f"Erro: Nenhuma opção de busca selecionada.")
        else:
            pass

        if opcoes == 'Substituir NCM.':
            ncm1 = self.txt_alt_NCM1.text()
            ncm2 = self.txt_alt_NCM2.text()
            print(ncm1, ncm2)
            self.update_ncm(ncm1,ncm2)

    def search_by_ncm(self):
        # Obtém o NCM digitado pelo usuário
        buscar_ncm = self.txt_buscar_ncm.text()

        # Carrega os NCMs expirados do arquivo JSON
        expired_ncms = self.processing_ncms_json()

        # Carrega os dados da planilha CSV
        csv_data = self.processing_ncm_csv()

        # Define o nome da coluna onde os NCMs estão localizados
        col_ncm_name = 'NCM'  # Substitua 'NCM' pelo nome real da coluna

        # Encontra o índice da coluna com o nome desejado
        try:
            col_ncm = next(i for i, col_name in enumerate(csv_data[0]) if col_name == col_ncm_name)
        except StopIteration:
            self.show_error_popup("Erro!", f"Coluna '{col_ncm_name}' não encontrada na planilha.")
            return

        # Filtra as linhas da planilha que contêm o NCM digitado pelo usuário
        rows_with_ncm = [row for row in csv_data if row[col_ncm] == buscar_ncm]

        # Atualiza a tabela com as linhas que contêm o NCM digitado pelo usuário
        self.update_table(rows_with_ncm, col_ncm=col_ncm, highlight_expired=True, expired_ncms=expired_ncms)

    #REALIZA A BUSCA POR NCMS INVÁLIDOS
    def search_invalid_ncm(self):
        # Carrega os NCMs expirados do arquivo JSON
        expired_ncms = self.processing_ncms_json()

        # Carrega os dados da planilha CSV
        csv_data = self.processing_ncm_csv()

        # Define o nome da coluna onde os NCMs estão localizados
        col_ncm_name = 'NCM'  # Substitua 'NCM' pelo nome real da coluna

        # Encontra o índice da coluna com o nome desejado
        try:
            col_ncm = next(i for i, col_name in enumerate(csv_data[0]) if col_name == col_ncm_name)
        except StopIteration:
            self.show_error_popup("Erro!", f"Coluna '{col_ncm_name}' não encontrada na planilha.")
            return

        # Filtra as linhas filtradas que contêm NCMs expirados
        expired_ncms_in_csv = [row for row in csv_data if row[col_ncm] in expired_ncms]

        # Atualiza a tabela com as linhas que contêm NCMs expirados
        self.update_table(expired_ncms_in_csv, col_ncm=col_ncm)
    
    def update_table(self, data, col_ncm, highlight_expired=False, expired_ncms=None):
        if not data:
            self.tb_dados_csv.clearContents()
            self.tb_dados_csv.setRowCount(0)
            self.tb_dados_csv.setColumnCount(0)
            self.txt_output_logs.appendPlainText("\nNenhum dado encontrado. Tabela limpa.")
            return
        
        num_rows = len(data)
        num_cols = len(data[0])

        self.tb_dados_csv.setRowCount(num_rows)
        self.tb_dados_csv.setColumnCount(num_cols)

        try:
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(cell_data)
                    self.tb_dados_csv.setItem(row_idx, col_idx, item)
                    if col_idx == col_ncm:
                        item.setForeground(QColor(255, 0, 0))  # Define a cor do texto para vermelho
                    if highlight_expired and expired_ncms and cell_data in expired_ncms:
                        item.setForeground(QColor(255, 0, 0))  # Define a cor do texto para vermelho

            self.txt_output_logs.appendPlainText("Tabela atualizada com NCMs expirados.")
        except Exception as e:
            self.txt_output_logs.appendPlainText(f"Erro ao atualizar tabela: {e}")
            self.show_error_popup("Erro!", f"Erro ao atualizar tabela: {e}")


    def update_ncm(self, old_ncm, new_ncm):
        try:
            # Carrega os dados da planilha CSV
            csv_data = self.processing_ncm_csv()

            # Define o índice da coluna NCM
            col_ncm = 0  # Assumindo que a coluna do NCM é a primeira (índice 0). Ajuste conforme necessário.

            # Atualiza os dados na planilha
            for row_idx, row_data in enumerate(csv_data):
                if row_data[col_ncm] == old_ncm:
                    csv_data[row_idx][col_ncm] = new_ncm

            # Escreve os dados atualizados de volta no arquivo CSV
            with open(self.path_csv, 'w', newline='') as file_csv:
                csv_writer = csv.writer(file_csv, delimiter=';')
                csv_writer.writerows(csv_data)

            self.txt_output_logs.appendPlainText(f"NCM '{old_ncm}' substituído por '{new_ncm}'. Tabela atualizada.")
        except Exception as e:
            self.txt_output_logs.appendPlainText(f"Erro ao atualizar NCM: {e}")
            self.show_error_popup("Erro!", f"Erro ao atualizar NCM: {e}")



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Processing_CSV()
    window.show()
    sys.exit(app.exec())

