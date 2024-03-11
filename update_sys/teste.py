import zipfile
import requests
from tqdm import tqdm
import sys
import os


directory_version = os.path.join("..","venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\version.txt")
destiny_path = 'C:\\Tech Tools'

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

verificar_atualizacoes()