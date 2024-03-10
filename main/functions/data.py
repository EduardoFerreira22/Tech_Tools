import sqlite3

class SQLite_Data():
    def conect_db(self):
        self.conn = sqlite3.connect('venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\techtools.db')

    def conect_close(self):
        try:
            self.conn.close()
        except:
            pass
    
    #########################################################################################################
    #DRIVERS IMPRESSORAS
    def select_printers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DESCRICAO FROM DRIVERS ORDER BY DESCRICAO")
            drivers = cursor.fetchall()
            return drivers
        except:
            pass

    def select_printer_tables(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT idDRIVER,DESCRICAO, LINK_DRIVER FROM DRIVERS WHERE DESCRICAO = '{name}'")
            drivers = cursor.fetchall()
            return drivers
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None
        
    def new_printer(self,name,link):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO DRIVERS(DESCRICAO, LINK_DRIVER) VALUES ('{name}','{link}')")
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None

        
    def update_printers(self, name, link,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"UPDATE DRIVERS SET DESCRICAO = '{name}', LINK_DRIVER = '{link}' WHERE idDRIVER = {id}")
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None


    #########################################################################################################
    #INATALADORES
    def select_instalers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DESCRICAO FROM INSTALADORES ORDER BY DESCRICAO")
            instalers = cursor.fetchall()
            return instalers
        except:
            pass

    def select_instalers_tables(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT idARQUIVO,DESCRICAO, LINK_ARQUIVO FROM INSTALADORES WHERE DESCRICAO = '{name}'")
            installs = cursor.fetchall()
            return installs
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None
        
    def new_istaler(self,name,link):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO INSTALADORES(DESCRICAO, LINK_ARQUIVO) VALUES ('{name}','{link}')")
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None

        
    def update_instaler(self, name, link,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"UPDATE INSTALADORES SET DESCRICAO = '{name}', LINK_ARQUIVO = '{link}' WHERE idARQUIVO = {id}")
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None

    #########################################################################################################
    #
    def select_scripts(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DESCRICAO FROM SCRIPTS ORDER BY DESCRICAO")
            scripts = cursor.fetchall()
            return scripts
        except:
            pass

    def combo_script_itens(self,name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT idSCRIPT,DESCRICAO,SCRIPT_TEXT FROM SCRIPTS WHERE DESCRICAO = '{name}'")
            infor = cursor.fetchall()
            return infor
        except:
            pass
    def new_script(self, name, script):
        try:
            query_script = "INSERT INTO SCRIPTS (DESCRICAO, SCRIPT_TEXT) VALUES (?, ?)"
            cursor = self.conn.cursor()
            cursor.execute(query_script, (name, script))
            self.conn.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None

    def update_script(self, name, script, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'UPDATE SCRIPTS SET DESCRICAO = "{name}", SCRIPT_TEXT = "{script}" WHERE idSCRIPT = {id}')
            self.conn.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None

        
    def delete_script(self,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM SCRIPTS WHERE idSCRIPT = {id}")
            cursor.connection.commit()
            return "OK"
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None