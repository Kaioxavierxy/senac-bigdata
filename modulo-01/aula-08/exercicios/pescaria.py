# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.

VALOR_P_QUILOS = 4
QTD_MAX = 100

def calcular_multa(peso_total):
    valor_multa = 0 

    if(peso_total > QTD_MAX):
        peso_excedente = peso_total - QTD_MAX
        valor_multa = peso_excedente * VALOR_P_QUILOS
        return valor_multa
    else:
      return valor_multa

#print(calcular_multa(130))
valor_total_multa = []

while True:
    peso_pesca = int(input("Qual o peso da sua pescária? "))
    
    if(peso_pesca == 0):
        multas = sum(valor_total_multa)
        if(multas != 0):
            print("O peso excedido em uma das pescas, valor da multa: ", multas)
        else:
            print("Peso dentro do limite. Nenhuma multa a pagar")
        break
    
    valor_total_multa.append(calcular_multa(peso_pesca))
