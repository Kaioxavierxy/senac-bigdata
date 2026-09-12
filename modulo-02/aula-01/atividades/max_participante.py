import pandas as pd
import numpy as np
import openpyxl

df_transacoes = pd.read_excel('../base_invest.xlsx', sheet_name='Transacoes')
df_participantes = pd.read_excel('../base_invest.xlsx', sheet_name='Participante')
df_ativos = pd.read_excel('../base_invest.xlsx', sheet_name='Ativo')

transacoes_participante1 = df_transacoes.loc[(df_transacoes['id_participante'] == 100)]

# O python permite encadeamento de funções
compras_participante = transacoes_participante1.loc[(transacoes_participante1['operacao'] == 'compra')]
compras_participante['valor_total'] = compras_participante['quantidade'] * compras_participante['preco']

valor_por_ativo = compras_participante.groupby('id_ativo')['valor_total'].sum()

id_ativo_maior_valor = valor_por_ativo.idxmax()
cnpj_maior_valor = df_ativos[df_ativos['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print(cnpj_maior_valor)

#print(transacoes_participante1)
#print('-'* 40)
#print(transacoes_participante2)
#print('-'* 40)
#print(transacoes_participante3)

#print(df_participantes)
