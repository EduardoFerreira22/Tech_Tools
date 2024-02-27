from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QInputDialog,QMessageBox,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
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
        self.comboBox_op_busca.currentIndexChanged.connect(self.combo_op_busca)
        self.bt_buscar_filecsv.clicked.connect(self.buscar_arquivo)
        self.bt_processar_arquivo_csv.clicked.connect(self.processar_csv)
        # self.bt_buscar_opcoes.clicked.connect(self.combo_op_busca)

        #PROCESSAMENTO
        self.comboBox_op_processamentos.currentIndexChanged.connect(self.combo_op_processamento)
        self.bt_executar_process.clicked.connect(self.exetuc_process)
        #VISIBILIDADE DOS BOTÕES ################################################################################
        self.bt_executar_combo_process.setVisible(False)
        self.bt_executar_process.setVisible(False)
        self.bt_setas_ncm.setVisible(False)
        self.bt_buscar_opcoes.setVisible(False)
        #VISIBILIDADE DOS ENTRYS ################################################################################
        self.txt_buscar_ncm.setVisible(False)
        self.txt_alt_NCM1.setVisible(False)
        self.txt_alt_NCM2.setVisible(False)
        #VISIBILIDADE DOS ComboBox ################################################################################
        self.combo_column1.setVisible(False)
        self.combo_column2.setVisible(False)
        #VISIBILIDADE DOS Label's ################################################################################
        self.lb_atencao_substituir.setVisible(False)
        self.lb_info_ncm_subst.setVisible(False)

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def buscar_arquivo(self):
        self.txt_output_logs.appendPlainText("Buscando novo arquivo.")
        #Abre um diálogo de seleção de arquivos
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Arquivo CSV UTF-8 (*.csv);;CSV separado por vírgula (*.csv)")

        if file_dialog.exec():
            #Obtém o caminho do arquivo selecionado
            selected_file = file_dialog.selectedFiles()[0]

            #Define o caminho do arquivo dentro do QLineEdit
            self.txt_path_filecsv.setText(selected_file)
            self.txt_output_logs.appendPlainText(f"\nCaminho do arquivo selecionado:\n{selected_file}")

    #ABRE E PROCESSA O ARQUIVO CSV
    def processar_csv(self):
        self.txt_output_logs.appendPlainText("\nIniciando leitura...")
  
        self.path_csv = self.txt_path_filecsv.text()

        if self.path_csv == '':
            self.txt_output_logs.appendPlainText("Erro: Usuário tentou processar, sem ter selecionado um arquivo antes.")
            self.show_error_popup("Atenção!", "Não é possível processar antes do usuário selecionar o arquivo.csv")
        else:
            self.txt_output_logs.appendPlainText("\nDados na tela.")
            self.txt_output_logs.appendPlainText(f"\nProcessando arquivo CSV")
            try:
                encodings = ['utf-8', 'latin1']
                for encoding in encodings:
                    try:
                        # Abre o arquivo e lê
                        with open(self.path_csv, 'r', newline='', encoding=encoding) as file_csv:
                            csv_reader = csv.reader(file_csv, delimiter=';')  # Especifica o delimitador como ponto e vírgula
                            csv_data = list(csv_reader)  # Lê todos os dados do CSV para uma lista

                        self.header = csv_data[0]
                        num_cols = len(self.header)
                        num_rows = len(csv_data) - 1  # Desconta o cabeçalho

                        self.tb_dados_csv.setRowCount(num_rows)
                        self.tb_dados_csv.setColumnCount(num_cols)
                        self.tb_dados_csv.setHorizontalHeaderLabels(self.header)

                        # Preenche a tabela com os dados
                        for row_idx, row_data in enumerate(csv_data[1:], 1):  # Começa da segunda linha
                            for col_idx, cell_data in enumerate(row_data):
                                item = QTableWidgetItem(cell_data)
                                self.tb_dados_csv.setItem(row_idx - 1, col_idx, item)  # Adiciona 1 ao índice de linha para começar da linha 2
                        self.txt_output_logs.appendPlainText("\nDados do arquivo CSV inseridos na tabela com sucesso.")
                        self.combo_Columns(head=self.header)
                        break  # Para a execução se a leitura for bem-sucedida
                    except Exception as e:
                        # Se ocorrer um erro, continue para tentar a próxima codificação
                        continue

                else:
                    # Se nenhuma codificação funcionar, mostra uma mensagem de erro
                    self.show_error_popup("Erro!", "Não foi possível abrir o arquivo CSV.")
            except Exception as e:
                self.txt_output_logs.appendPlainText(f"Erro:\n{e}")

    #ABRE E PROCESSA O ARQUIVO JSON
    def processing_ncms_json(self):
        try:
            with open('resource\\EXPIRED_NCM.json', 'r', encoding='utf-8') as f:
                expired_ncms_data = json.load(f)
                expired_ncms = [ncm['Codigo'] for ncm in expired_ncms_data.get('Nomenclaturas', [])]
                return expired_ncms
        except FileNotFoundError:
            self.show_error_popup("Erro!", "Arquivo 'EXPIRED_NCM.json' não encontrado.")

    def processing_ncm_csv(self):
        path_csv = self.txt_path_filecsv.text()
        try:
            encodings = ['utf-8', 'latin1']
            for encoding in encodings:
                try:
                                # Abre o arquivo e lê
                    with open(path_csv, 'r',encoding=encoding) as file_csv:
                        csv_reader = csv.reader(file_csv, delimiter=';')
                        csv_data = [row for row in csv_reader]  # Lê todos os dados do CSV
                        return csv_data
                except Exception as e:
                        # Se ocorrer um erro, continue para tentar a próxima codificação
                    continue
        except Exception as e:
            self.show_error_popup("Erro!", "Arquivo csv não encontrado.")
    
    #OPÇÕES DE BUSCA
    def combo_op_busca(self):
        opcoes = self.comboBox_op_busca.currentText()
        self.txt_output_logs.appendPlainText(f"\nOpção selecionada: {opcoes}")
        if opcoes == '':
            self.show_error_popup("Erro!", f"É necessário selecionar uma das opções antes de realizar a busca.")
            self.txt_output_logs.appendPlainText(f"Erro: Nenhuma opção de busca selecionada.")
        else:
            pass

        if opcoes == 'Buscar por NCM':
            self.bt_buscar_opcoes.setVisible(True)
            self.txt_buscar_ncm.setVisible(True)
            self.bt_buscar_opcoes.clicked.connect(self.search_by_ncm)
        elif opcoes == "Buscar NCM's inválidos.":
            self.txt_buscar_ncm.setVisible(False)
            self.bt_buscar_opcoes.setVisible(False)
            self.search_invalid_ncm()
        elif opcoes == 'Tudo que contém.':
            self.txt_buscar_ncm.setVisible(True)
            self.bt_buscar_opcoes.setVisible(True)
            self.bt_buscar_opcoes.clicked.connect(self.tudo_que_contem)

    # OPÇÕES DE PROCESSAMENTO 
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
            self.combo_column1.setVisible(False)
            self.combo_column2.setVisible(False)
            self.bt_setas_ncm.setVisible(True)
            self.bt_executar_process.setVisible(True)
            self.lb_info_ncm_subst.setVisible(True)


        elif opcoes == 'Tudo que contém mude para':
            self.lb_atencao_substituir.setVisible(True)
            self.txt_alt_NCM1.setVisible(True)
            self.txt_alt_NCM2.setVisible(True)
            self.bt_setas_ncm.setVisible(True)
            self.combo_column1.setVisible(False)
            self.combo_column2.setVisible(False)
            self.bt_executar_process.setVisible(True)
        
        elif opcoes == 'P. X da Coluna A , Coluna B Recebe':
            self.combo_column1.setVisible(True)
            self.combo_column2.setVisible(True)
            self.txt_alt_NCM1.setVisible(True)
            self.txt_alt_NCM2.setVisible(True)
            self.bt_setas_ncm.setVisible(True)
            self.bt_executar_process.setVisible(True)
            self.lb_atencao_substituir.setVisible(True)
            print(opcoes)

            self.bt_executar_process.clicked.connect(self.column1_alter_column2)
    #COMBO OPTIONS
    def combo_Columns(self,head):
        self.combo_column1.addItems(head)
        self.combo_column2.addItems(head)

    # EXECUTA 
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

        elif opcoes == 'Tudo que contém mude para':
            self.process_tudo_que_contem()

    def search_by_ncm(self):
        buscar_ncm = self.txt_buscar_ncm.text()

        # Carrega os NCMs expirados do arquivo JSON
        expired_ncms = self.processing_ncms_json()

        # Carrega os dados da planilha CSV
        csv_data = self.processing_ncm_csv()

        # Define uma lista de possíveis nomes de coluna onde os NCMs podem estar localizados
        possiveis_nomes_coluna = ['NCM', 'id_ncm', 'Ncm', 'Codigo_ncm']

        # Encontra o índice da coluna com o nome desejado
        col_ncm = None
        for nome_coluna in possiveis_nomes_coluna:
            try:
                col_ncm = next(i for i, col_name in enumerate(csv_data[0]) if col_name.lower() == nome_coluna.lower())
                break  # Sai do loop se o índice da coluna for encontrado
            except StopIteration:
                continue  # Continua para o próximo nome de coluna se a atual não for encontrada

        if col_ncm is None:
            self.show_error_popup("Erro!", f"Nenhum dos nomes de coluna ({', '.join(possiveis_nomes_coluna)}) encontrado na planilha.")
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

        # Define uma lista de possíveis nomes de coluna onde os NCMs podem estar localizados
        possiveis_nomes_coluna = ['NCM', 'id_ncm', 'Ncm', 'Codigo_ncm']

        # Encontra o índice da coluna com o nome desejado
        col_ncm = None
        for nome_coluna in possiveis_nomes_coluna:
            try:
                col_ncm = next(i for i, col_name in enumerate(csv_data[0]) if col_name.lower() == nome_coluna.lower())
                break  # Sai do loop se o índice da coluna for encontrado
            except StopIteration:
                continue  # Continua para o próximo nome de coluna se a atual não for encontrada

        if col_ncm is None:
            self.show_error_popup("Erro!", f"Nenhum dos nomes de coluna ({', '.join(possiveis_nomes_coluna)}) encontrado na planilha.")
            return

        # Filtra as linhas da planilha que contêm NCMs expirados
        expired_ncms_in_csv = [row for row in csv_data if row[col_ncm] in expired_ncms]

        # Atualiza a tabela com as linhas que contêm NCMs expirados
        self.update_table(expired_ncms_in_csv, col_ncm=col_ncm)
    #ATUALIZA A TABELA APÓS ALGUMA INTERAÇÃO
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
    # ATUALIZA A UM NCM POR OUTRO
    def update_ncm(self, ncm1, ncm2):
        try:
            encodings = ['utf-8', 'latin1']
            for encoding in encodings:
                try:
                    # Carrega os dados da planilha CSV
                    with open(self.path_csv, 'r', newline='', encoding=encoding) as file:
                        reader = csv.reader(file, delimiter=';')
                        csv_data = list(reader)

                    # Procurar a coluna que contém o NCM
                    possible_ncm_columns = ['NCM', 'ncm', 'Ncm', 'Codigo_ncm', 'Codigo_Ncm', 'CODIGO_NCM']
                    col_ncm = None
                    for i, header in enumerate(csv_data[0]):
                        if header in possible_ncm_columns:
                            col_ncm = i
                            break

                    if col_ncm is None:
                        print("Nenhuma coluna de NCM encontrada no arquivo CSV.")
                        self.txt_output_logs.appendPlainText("Nenhuma coluna de NCM encontrada no arquivo CSV.")
                        return

                    # Lista para armazenar os nomes das colunas
                    headers = csv_data[0]

                    # Lista para armazenar as linhas modificadas
                    linhas_modificadas = []

                    # Iterar sobre os dados do CSV
                    for linha in csv_data:
                        # Verificar se o NCM antigo existe na linha
                        if linha[col_ncm] == ncm1:
                            print(f"NCM antigo encontrado: {ncm1}")
                            self.txt_output_logs.appendPlainText(f"NCM antigo encontrado: {ncm1}")
                            # Substituir o NCM antigo pelo novo NCM
                            linha[col_ncm] = ncm2
                            linhas_modificadas.append(linha)
                    self.txt_output_logs.appendPlainText(f"Novo NCM: {ncm2} gravado com sucesso!")
                    # Escrever os dados atualizados de volta para o arquivo CSV
                    with open(self.path_csv, 'w', newline='', encoding=encoding) as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(csv_data)

                    # Limpar completamente a tabela antes de atualizá-la com as linhas modificadas
                    self.tb_dados_csv.clear()

                    # Definir os cabeçalhos da tabela
                    self.tb_dados_csv.setColumnCount(len(headers))
                    self.tb_dados_csv.setHorizontalHeaderLabels(headers)

                    # Atualizar a tabela apenas com as linhas modificadas
                    if linhas_modificadas:
                        self.tb_dados_csv.setRowCount(len(linhas_modificadas))
                        for row_idx, row_data in enumerate(linhas_modificadas):
                            for col_idx, cell_data in enumerate(row_data):
                                item = QTableWidgetItem(str(cell_data))
                                self.tb_dados_csv.setItem(row_idx, col_idx, item)
                    else:
                        print("Nenhuma linha modificada encontrada.")
                        self.txt_output_logs.appendPlainText("Nenhuma linha modificada encontrada.")
                        
                    # Saia do loop se os dados foram atualizados com sucesso
                    break
                except Exception as e:
                    # Se ocorrer um erro, continue para tentar a próxima codificação
                    continue
        except Exception as e:
            self.txt_output_logs.appendPlainText(f"Erro ao atualizar NCM: {e}")
            print(f"Erro ao atualizar NCM: {e}")

    # SE COLUNA A EXISTE MUDE DADOS DA COLUNA B,C
    def column1_alter_column2(self):
        coluna_combobox1 = self.combo_column1.currentIndex()  # Índice da coluna selecionada no combobox 1
        coluna_combobox2 = self.combo_column2.currentIndex()  # Índice da coluna selecionada no combobox 2
        dado_entrada1 = self.txt_alt_NCM1.text()            # Dado digitado na entrada 1
        dado_entrada2 = self.txt_alt_NCM2.text()            # Dado digitado na entrada 2

        load_data = self.processing_ncm_csv()

        # Lista para armazenar os resultados
        resultados = []

        # Iterar sobre os dados do CSV
        for linha in load_data:
            # Verificar se o dado digitado na entrada 1 existe na coluna selecionada no combobox 1
            if linha[coluna_combobox1].lower() == dado_entrada1.lower():
                # Substituir o dado na coluna selecionada no combobox 2 pelo dado digitado na entrada 2
                linha[coluna_combobox2] = dado_entrada2
            # Adicionar a linha aos resultados, independentemente de ter sido modificada ou não
            resultados.append(linha)

        # Atualizar a tabela com os novos dados
        self.update_table_process(resultados)
        # Escrever os dados atualizados de volta para o arquivo CSV
        self.write_to_csv(resultados)

    def update_table_process(self, data):
        # Limpar a tabela antes de atualizá-la com os novos dados
        self.tb_dados_csv.clearContents()
        # Preencher a tabela com os novos dados
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tb_dados_csv.setItem(row_idx - 1, col_idx, item)

    def tudo_que_contem(self):
        # Pega o dado digitado
        search = self.txt_buscar_ncm.text()

        # Carrega os dados da planilha
        load_data = self.processing_ncm_csv()

        # Lista para armazenar os resultados
        resultados = []

        # Itera sobre as linhas do arquivo CSV
        for row in load_data:
            # Verifica se o texto digitado está presente em alguma célula da linha
            if any(search.lower() in cell.lower() for cell in row):
                resultados.append(row)  # Adiciona a linha aos resultados se encontrar uma correspondência

        # Limpa completamente a tabela
        self.tb_dados_csv.clear()

        # Imprime os resultados na tabela
        if resultados:
            # Defina os cabeçalhos da tabela
            if self.header:
                self.tb_dados_csv.setColumnCount(len(self.header))
                self.tb_dados_csv.setHorizontalHeaderLabels(self.header)

            # Adiciona as linhas dos resultados à tabela
            self.tb_dados_csv.setRowCount(len(resultados))
            for row_idx, row_data in enumerate(resultados):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.tb_dados_csv.setItem(row_idx, col_idx, item)
        else:
            print("Nenhum resultado encontrado.")

    def process_tudo_que_contem(self):
        data1 = self.txt_alt_NCM1.text()
        data2 = self.txt_alt_NCM2.text()
        # Lista para armazenar as linhas atualizadas
        linhas_atualizadas = []
        try:
            encodings = ['utf-8', 'latin1']
            for encoding in encodings:
                try:
                    # Abrir o arquivo CSV em modo de leitura e escrita
                    with open(self.path_csv, 'r', newline='',encoding=encoding) as file:
                        reader = csv.reader(file, delimiter=';')

                        # Percorrer as linhas do arquivo CSV
                        for row in reader:
                            # Substituir o dado a ser buscado pelo dado substituto em cada célula da linha
                            nova_linha = [celula.replace(data1, data2) for celula in row]
                            linhas_atualizadas.append(nova_linha)

                    # Reescrever o arquivo CSV com as linhas atualizadas
                    with open(self.path_csv, 'w', newline='', encoding=encoding) as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(linhas_atualizadas)

                    self.update_table_process(linhas_atualizadas)
                except Exception as e:
                        # Se ocorrer um erro, continue para tentar a próxima codificação
                    continue
            
        except Exception as e:
            self.txt_output_logs.appendPlainText(f"Erro ao gravar dados no arquivo CSV: {e}")
            print(f"Erro ao gravar dados no arquivo CSV: {e}")

    def write_to_csv(self, data):
        try:
            encodings = ['utf-8', 'latin1']
            for encoding in encodings:
                try:
                    # Ler os dados originais do CSV
                    with open(self.path_csv, 'r', newline='', encoding=encoding) as file:
                        reader = csv.reader(file)
                        original_data = list(reader)
                    
                    # Atualizar apenas as linhas modificadas
                    for i, linha in enumerate(original_data):
                        if i < len(data):
                            original_data[i] = data[i]

                    # Escrever os dados atualizados de volta para o arquivo CSV
                    with open(self.path_csv, 'w', newline='', encoding=encoding) as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(original_data)
                    
                    print("Dados gravados com sucesso no arquivo CSV.")
                    self.txt_output_logs.appendPlainText("Dados gravados com sucesso no arquivo CSV.")
                except Exception as e:
                        # Se ocorrer um erro, continue para tentar a próxima codificação
                    continue
            
        except Exception as e:
            self.txt_output_logs.appendPlainText(f"Erro ao gravar dados no arquivo CSV: {e}")
            print(f"Erro ao gravar dados no arquivo CSV: {e}")

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Processing_CSV()
    window.show()
    sys.exit(app.exec())

