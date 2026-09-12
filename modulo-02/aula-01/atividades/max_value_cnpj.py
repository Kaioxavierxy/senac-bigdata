import pandas as pd
import numpy as np
import openpyxl

# operacoes_compra = df.loc[(df['operacao'] == 'compra')]
df = pd.read_excel('../base_invest.xlsx', sheet_name='Transacoes')

operacoes_compra = df.loc[(df['operacao'] == 'compra')]


print(operacoes_compra)
