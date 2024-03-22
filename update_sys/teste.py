import os
import re

def buscar_arquivo_extraido():
    try:
        caminho = 'C:\\Tech Tools'
        for file_name in os.listdir(caminho):
            print(f"Nome do arquivo: {file_name}")
            if re.match(r"EduardoFerreira22-Tech_Tools-\w+", file_name):
                pre_fixo = file_name[len("EduardoFerreira22-Tech_Tools-"):].strip()
                fixo = pre_fixo
                print(f"Prefixo encontrado: {fixo}")
                return fixo
    except Exception as e:
        print(f"Erro: {e}")

print(buscar_arquivo_extraido())
