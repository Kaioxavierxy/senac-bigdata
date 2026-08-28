# Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
# pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
# ● Fórmula: IMC = PESO / (ALTURA * ALTURA)
# ● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
# os valores e retornará o IMC calculado.
# ● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
# valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
# ○ Valores de Referência:
# ■ Menor que 18.5: "Abaixo do peso"
# ■ 18.5 a 24.9: "Peso normal"
# ■ 25.0 a 29.9: "Sobrepeso"
# ■ 30.0 ou mais: "Obesidade"
# ● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
# chamar as duas funções e imprimir o resultado formatado.

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def obter_classificacao(imc): 
    if(imc < 18.5):
        print("Abaixo da peso")
    elif(imc >= 25.0 and imc <= 29.9):
        print("Sobrepeso")
    elif(imc >= 30.0):
        print("Obesidade")
    else:
     print("Seu peso está normal")

while True:
    try:
     peso = float(input("Qual é a sua peso? (Digite 0 para sair do sistema) "))
     altura = float(input("Qual é a sua altura? (Digite zero para sair do sistema) "))
    except ValueError:
        print("Erro! O valor digitado precisa ser um número!")

    obter_classificacao(calcular_imc(peso, altura))
