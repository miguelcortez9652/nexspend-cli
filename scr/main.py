import pandas as pd
import os

arquive_csv = "data/exemplo.csv"


try:
    if not os.path.isfile(arquive_csv):
        raise FileNotFoundError(f"File not found: {arquive_csv}")
    
    df = pd.read_csv(arquive_csv, encoding="utf-8", sep =",")


    print("Primeiras linhas do arquivo:")
    print(df.head())
except FileNotFoundError as e:
    print(e)
except pd.errors.EmptyDataError:
    print("O arquivo está vazio.")
except pd.errors.ParserError:
    print("Erro ao processar o arquivo CSV. Verifique o formato.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")