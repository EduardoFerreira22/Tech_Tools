import os
import requests
import shutil
import tkinter as tk
from tkinter import messagebox
import git
from tqdm import tqdm
import zipfile

def get_latest_release():
    url = "https://api.github.com/repos/EduardoFerreira22/Tech_Tools/releases/latest"
    response = requests.get(url)
    data = response.json()
    return data["tag_name"]

def install_update(root):
    repo = git.Repo.clone_from("https://github.com/EduardoFerreira22/Tech_Tools.git", "temp")
    
    # Copia os novos arquivos para o diretório de instalação
    dest_directory = "C:\\Tech_Tools"
    for item in os.listdir("temp"):
        source = os.path.join("temp", item)
        destination = os.path.join(dest_directory, item)
        if os.path.exists(destination):
            if os.path.isdir(destination):
                shutil.rmtree(destination)
            else:
                os.remove(destination)
        shutil.move(source, destination)

    print("Atualização instalada com sucesso!")
    shutil.rmtree("temp")  # Remove a pasta "temp"
    root.destroy()  # Fecha a janela após a instalação

def main():
    current_version = "0.0"  # Sua versão atual
    latest_release = get_latest_release()

    if not latest_release:
        # Não há lançamentos disponíveis
        messagebox.showinfo("Atualização", "Não há atualizações disponíveis no momento!")
        return

    if latest_release > current_version:
        root = tk.Tk()
        root.geometry("300x150")
        root.title("Atualização")

        label = tk.Label(root, text=f"Nova versão disponível: {latest_release}\nDeseja instalar agora?")
        label.pack()

        # Função para chamar a instalação com o fechamento da janela
        def install_with_close():
            install_update(root)

        bt_yes = tk.Button(root, text="SIM", width=10, command=install_with_close)
        bt_yes.place_configure(x=65, y=100)

        bt_no = tk.Button(root, text="NÃO", width=10, command=root.destroy)
        bt_no.place_configure(x=160, y=100)

        root.mainloop()
    else:
        print("Você já está usando a versão mais recente.")

if __name__ == "__main__":
    main()
