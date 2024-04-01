from datetime import datetime
import logging
import inspect
import os


class App_logs:
    def __init__(self):
        self.logger = None


    def logs(self,name_file,path, msg):
        # Verifica se a pasta logs_main existe, caso contrário, cria
        
        if not os.path.exists(path):
            os.makedirs(path)

        # Formato do Log
        if not self.logger:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)

            # Criando um novo arquivo de log na pasta logs_main
            file_name = os.path.join(path, f"{name_file}_{datetime.now().strftime('%d-%m-%y')}.txt")
            file_handler = logging.FileHandler(file_name)
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        # Registrando a mensagem no log
        self.logger.info(msg)
