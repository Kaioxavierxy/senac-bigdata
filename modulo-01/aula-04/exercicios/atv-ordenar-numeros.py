lista = []

while True:
     try:
        number1 = int(input("Escolha o primeiro numero"))
        if(number1 != int): 
          print("Erro! O número digitado precisa ser um número!")
        lista.append(number1)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")

while True:
     try:
        number2 = int(input("Escolha o segundo numero"))
        if(number2 != int): 
          print("Erro! O número digitado precisa ser um número!")
        lista.append(number2)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")

while True:
     try:
        number3 = int(input("Escolha o terceiro numero"))
        if(number3 != int): 
          print("Erro! O número digitado precisa ser um número!")
        lista.append(number3)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")
    
lista.sort()
print(lista)