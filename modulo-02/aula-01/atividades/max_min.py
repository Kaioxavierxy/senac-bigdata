import pandas as pd
import numpy as np
import openpyxl

#df.loc[(df["max_speed"] > 4) | (df["shield"] < 5)]

#A utilização de ambos recursos é útil, porem loc se mostra mais versátil, pois podemos selecionar colunas pela nomenclatura delas o que torna o trabalho mais fácil;

df = pd.read_excel('../base_invest.xlsx')
operacoes_compra = df.loc[(df['operacao'] == 'compra')]
operacoes_venda = df.loc[(df['operacao'] == 'venda')]
# operacoes_compra = df.query["operacao == compra"]

# Valores maximos e minimos:
maximo_compra = operacoes_compra.max()
minimo_compra = operacoes_compra.min()

maximo_venda = operacoes_venda.max()
minimo_venda = operacoes_venda.min()

print("A operação maxima e minima de compra é: ", maximo_compra['preco'] ,"e", minimo_compra['preco'])
print("A operação maxima e minima de venda é: ", maximo_venda['preco'] ,"e", minimo_venda['preco'])