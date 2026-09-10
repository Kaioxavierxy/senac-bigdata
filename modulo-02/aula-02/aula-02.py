import pandas as pd  # alias 'pd'
import numpy as np   # alias 'np'

#LOC 
#ILOC
#QUERY

filmes = {
    'título': ["Lagoa Azul", "Agente Secreto", "Gênio Indomável", "A Freira", "Brinquedo Assassino", "Top Gun"],
    'categoria': ["Romance", "Ação", "Drama", "Terror", "Comédia", "Aventura"],
    'ano': ["1980", "2025", "1997", "2022", "1995", "1986"],
    'faturamento': [6.5, 5, 4, 5.5, 3, 9],
}

indices = ['A', 'B', 'C', 'D', 'E', 'F']

tabela_de_filmes = pd.DataFrame(filmes, index=indices)
print(tabela_de_filmes)
print('-'*40)
#print(tabela_de_filmes.iloc[-1])
#print('-'*20)
print(tabela_de_filmes.iloc[1:3])
print('-'*40)

print(tabela_de_filmes.loc['B':'E'])
print('-'*20)

consulta1 = tabela_de_filmes.query['faturamento == 5']
print(consulta1)
# < > <= >= == != and or not in