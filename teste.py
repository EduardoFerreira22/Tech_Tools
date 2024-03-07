import os



def version_txt():
        path_txt = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\version.txt"
        try:
            if os.path.exists(path_txt):
                with open(path_txt, 'r') as r:
                    line = r.readline()
                    for line in r:
                        print(line)
                        if line.startswith("db_version:"):
                            v_db = line[len("db_version: "):].strip()
                            print(v_db)
                            return v_db
                    
        except Exception as e:
            print(f"Erro:\n{e}")

version_txt()