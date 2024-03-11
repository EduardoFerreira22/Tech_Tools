from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from ui_update import Ui_Updating
import zipfile
import requests
from tqdm import tqdm
import time
import sys
import shutil
import os




def verificar_atualizacoes():
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

        # Obtém a versão mais recente do programa
        ultima_versao = releases[0]["tag_name"]

        # Lê a versão atual do programa do arquivo "version.txt"
        # Diretório de instalação do Tech Tools
        diretorio_instalacao = ""

        if os.path.exists(directory_version):
            with open(directory_version, 'r') as file_version:
                version = file_version.readline()
                if version.startswith("Version_app:"):
                    arquivo_version = version[len("Version_app: "):].strip()
        else:
            # O arquivo não existe, então defina a versão atual como "0.0"
            arquivo_version = "0.0"

        # Compara as versões
        if ultima_versao > arquivo_version:
            # Há uma nova versão disponível
            resposta = input(
                f"Nova versão disponível ({ultima_versao})! Deseja atualizar? (S/N): ").lower()

            if resposta == "s":
                # Faz o download do arquivo zip do repositório no GitHub
                url_download = releases[0]["zipball_url"]
                response = requests.get(url_download, stream=True)

                total_size = int(response.headers.get("content-length", 100))
                block_size = 1024  # 1 Kibibyte

                print("Baixando atualização...")

                # Define o caminho para o arquivo zip
                arquivo_zip = os.path.join(diretorio_instalacao, "update.zip")

                # Faz o download do arquivo zip e exibe o progresso
                with open(arquivo_zip, "wb") as f:
                    bytes_downloaded = 0
                    for chunk in tqdm(response.iter_content(chunk_size=block_size), total=total_size/block_size, unit="KB"):
                        if chunk:
                            f.write(chunk)
                            bytes_downloaded += len(chunk)

                print("Download completo.")

                # Extrai os arquivos do zip
                with zipfile.ZipFile(arquivo_zip, "r") as zip_ref:
                    zip_ref.extractall(diretorio_instalacao)

                # Remove o arquivo zip
                os.remove(arquivo_zip)

                # Verifica se o arquivo principal existe
                arquivo_principal = os.path.join(
                    diretorio_instalacao, "main.py")
                if os.path.isfile(arquivo_principal):
                    # Executa o arquivo principal
                    os.startfile(arquivo_principal)
                else:
                    # O arquivo principal não existe
                    print("Erro: O arquivo principal não foi encontrado.")

                # Reinicia o programa para carregar a nova versão
                os.execv(sys.executable, [sys.executable] + sys.argv)

            else:
                print("Atualização cancelada.")
        else:
            print("Não há atualizações disponíveis.")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Não foi possível se conectar ao servidor. Verifique sua conexão com a internet e tente novamente.")


class Win_Update(QMainWindow,Ui_Updating):
    def __init__(self):
        super(Win_Update, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerenciador de atualizações Tech Tools")
        appIcon = QIcon(u"img\\TECH NEW LOGO.png")
        self.setWindowIcon(appIcon)
        self.setFixedSize(423, 180)
        self.destiny_path = 'C:\\Tech Tools'
        self.verificar_atualizacoes()

        self.progressBar_instalao.setVisible(False)
        self.bt_sim.clicked.connect(self.download_version)
        self.bt_nao.clicked.connect(app.closeAllWindows)
        self.download_timer = QTimer(self)
        self.download_timer.timeout.connect(self.update_progress)
        self.download_timer.start(5000)  # Define o intervalo em milissegundos (5 segundos)
        self.download_timer.setSingleShot(True)
    
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
                # Definindo a fonte e cor para o texto
                font = QFont()
                font.setPointSize(9)
                font.setBold(True)
                color = QColor(255, 255, 255)  # Cor branca

                # Aplicando as configurações ao label
                self.lb_version.setText(f'Versão {ultima_versao} já está disponível, deseja baixá-la?')
                self.lb_version.setFont(font)
                self.lb_version.setStyleSheet(f"color: rgb(255, 255, 255); text-align: center;")

                self.url_download = url_download  # Salva a URL para uso posterior
                print(self.url_download)
            else:
                self.lb_version.clear()

        except Exception as e:
            print(f"Erro: {e}")
    
    def download_version(self):
        self.progressBar_instalao.setVisible(True)
        try:
            # Simula um atraso de 10 segundos antes de iniciar o download
            time.sleep(10)
            
            response = requests.get(self.url_download, stream=True)
            self.arquivo_zip = os.path.join(self.destiny_path, 'TechTools.zip')
            with open(self.arquivo_zip, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        self.download_timer.start(1000)  # Inicia o temporizador de 5 segundos para atualizar a barra de progresso
            print("Download completo.")
            # Extrai os arquivos do zip
            with zipfile.ZipFile(self.arquivo_zip, "r") as zip_ref:
                zip_ref.extractall(self.destiny_path)
            # Chame a função copy_files com os diretórios de origem e destino
            source_dir = "C:\\Tech Tools\\EduardoFerreira22-Tech_Tools-c6bbe80"
            dest_dir = "C:\\Tech Tools"
            self.copy_files(source_dir, dest_dir)

        except Exception as e:
            print(f"Erro durante o download: {e}")

    def update_progress(self):
        # Verifica se o arquivo ZIP já foi baixado
        if hasattr(self, 'arquivo_zip'):
            total_size = os.path.getsize(self.arquivo_zip)
            bytes_downloaded = os.path.getsize(self.arquivo_zip)  # Obtém o tamanho atual do arquivo
            progress = (bytes_downloaded / total_size) * 100
            self.progressBar_instalao.setValue(progress)  # Atualiza o valor da barra de progresso
            QApplication.instance().processEvents()  # Força a atualização da interface gráfica

    def copy_files(self, source_dir, dest_dir):
        # Verifica se o diretório de origem existe
        if not os.path.exists(source_dir):
            print(f"Diretório de origem '{source_dir}' não existe.")
            return
        
        # Verifica se o diretório de destino existe, se não, cria
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        try:
            # Percorre todos os arquivos e pastas no diretório de origem
            for item in os.listdir(source_dir):
                # Constrói o caminho completo para o arquivo ou pasta
                source_item_path = os.path.join(source_dir, item)
                dest_item_path = os.path.join(dest_dir, item)

                # Verifica se é um arquivo
                if os.path.isfile(source_item_path):
                    # Verifica se o arquivo já existe no destino
                    if os.path.exists(dest_item_path):
                        os.remove(dest_item_path)  # Remove o arquivo existente
                    # Copia o arquivo para o diretório de destino
                    shutil.copy2(source_item_path, dest_item_path)
                    print(f"Arquivo '{item}' copiado para '{dest_dir}'")
                # Verifica se é uma pasta
                elif os.path.isdir(source_item_path):
                    # Copia o conteúdo da pasta recursivamente para o diretório de destino
                    self.copy_files(source_item_path, dest_item_path)
                    print(f"Conteúdo da pasta '{item}' copiado para '{dest_dir}'")

            print("Cópia de arquivos concluída com sucesso.")
        except Exception as e:
            print(f"Erro ao copiar arquivos: {e}")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Win_Update()
    window.show()
    sys.exit(app.exec())