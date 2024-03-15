import json

with open("resource\\NCM.json", 'r', encoding='utf-8') as f:
    cod_ncm = json.load(f)
    
meus_ncm = []
codigos = [ncm['Codigo'] for ncm in cod_ncm.get('Nomenclaturas', [])]
teste = codigos.append(meus_ncm)
print(meus_ncm)
