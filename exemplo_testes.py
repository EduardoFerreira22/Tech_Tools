import json

codigo = '0102.29.11'
with open("resource\\NCM.json", 'r', encoding='utf-8') as f:
    cod_ncm = json.load(f)

for ncm in cod_ncm.get('Nomenclaturas', []):
    if ncm['Codigo'] == codigo:
        print(f"Código: {ncm['Codigo']}")
        print(f"Descricao: {ncm['Descricao']}")