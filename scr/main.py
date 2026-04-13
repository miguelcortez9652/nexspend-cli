import pandas as pd
import os

csv_file = "data/exemplo.csv"


try:
		if not os.path.isfile(csv_file):
			raise FileNotFoundError(f"File not found: {csv_file}")

		df = pd.read_csv(csv_file, encoding="utf-8", sep =",")

		print("Primeiras linhas do arquivo:")
		print(df.to_string())
		#montante_final = df["Valor"].sum()
		number_of_transactions =len(df)
		print(f"Number of  transactions: {number_of_transactions}")
	# print(f"Transactions: {montante_final}")
		receita_total = df[df["Valor"]>0]["Valor"].sum()
		print(f"Total de receita: ${receita_total}")
		despesa_total = df[df["Valor"]<0]["Valor"].sum()
		print(f"Despesa total: ${-1*despesa_total}  ")

		print(f"Saldo final: ${receita_total - despesa_total}")









except FileNotFoundError as e:
    print(e)
except pd.errors.EmptyDataError:
    print("O arquivo está vazio.")
except pd.errors.ParserError:
    print("Erro ao processar o arquivo CSV. Verifique o formato.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


