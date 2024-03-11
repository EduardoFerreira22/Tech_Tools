directory_version = "venv\\Lib\\site-packages\\.DB\\.bd\\file_db\\file\\bd\\version.txt"

with open(directory_version, 'r') as file_version:
    version = file_version.readline()
    if version.startswith("Version_app:"):
        file = version[len("Version_app: "):].strip()
print(file) 