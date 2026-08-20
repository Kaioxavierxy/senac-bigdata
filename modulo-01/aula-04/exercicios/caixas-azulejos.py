#ara calcular a área de um retângulo, basta multiplicar o valor da base (comprimento) pelo valor da altura (largura). 
altura = int(input("Escolha a altura do comodo:"))
largura = int(input("Escolha a largura do comodo (Metros quadrados):"))
comprimento = int(input("Escolha o comprimento do comodo (Metros quadrados):"))

def calcularArea():
  comprimento_total_comodo = altura * comprimento * 4
  print(comprimento_total_comodo)

  comprimento_inicial = 0
  qtd_pisos = 0

  for i in range(comprimento_total_comodo):
    if(comprimento_inicial < comprimento_total_comodo):
        comprimento_inicial += 1.5
        qtd_pisos += 1

  print(comprimento_total_comodo)
  print(comprimento_inicial)
  print(qtd_pisos)


calcularArea()