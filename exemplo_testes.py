import pandas as pd
import csv

def valores_negativos_e_alterar(coluna, path):
    try:
        df = pd.read_csv(path, delimiter=';', encoding='utf-8')

        # Identificar e alterar os valores negativos para 0
        df.loc[df[coluna] < 0, coluna] = 0

        df.to_csv(path,index=False, sep=';', encoding='utf-8')
        print("Valores negativos substituídos por 0 com sucesso.")

        print(df)
                    
    except Exception as e:
        print(f"Erro: {e}")

caminho = 'produtos02.csv'
coluna = 'Estoque'
valores_negativos_e_alterar(coluna, caminho)
