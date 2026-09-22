import pandas as pd

df = pd.read_csv('vendas_produtos.csv')
print(df.head())

#####################

import mysql.connector

# 1. Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meu_ecomerce"
)

# 2. Criar um objeto cursor para executar as queries
cursor = conexao.cursor()

# 3. Definir a query
query = "SELECT * FROM produtos"

# 4. Executar a query
cursor.execute(query)

# 5. Obter os resultados
resultados = cursor.fetchall()

# 6. Exibir os resultados
for linha in resultados:
    print(linha)

# 7. Fechar a conexão
cursor.close()
conexao.close()

######################