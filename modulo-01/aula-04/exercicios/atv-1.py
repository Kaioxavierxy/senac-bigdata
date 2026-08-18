lista = [5, 2, 3]
newList = []

""" while True:
     try:
        number1 = int(input("Escolha o primeiro numero"))
        lista.append(number1)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")

while True:
     try:
        number2 = int(input("Escolha o segundo numero"))
        lista.append(number2)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")

while True:
     try:
        number3 = int(input("Escolha o terceiro numero"))
        lista.append(number3)
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.") """
    
def ArranjarLista():
   listaLenght = len(lista)
  
   for i in lista:
     if(len(newList) == 0):
        newList.append(i)

     if(i <= newList[(len(newList) - 1)]):
        newList.unshift(i)

ArranjarLista()


print(newList)