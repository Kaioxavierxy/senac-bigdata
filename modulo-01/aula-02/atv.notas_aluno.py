prova1 = {
    "matematica": 8,
    "portugues": 9,
    "historia": 10,
    "geografia": 10,
}
prova2 = {
    "matematica":5,
    "portugues": 6,
    "historia": 8,
    "geografia": 10,
}

class prova:
    def __init__(self, prova_1, prova_2):
        self.prova_1_notas = prova_1
        self.prova_2_notas = prova_2
        self.mediaProvas_notas = { }

    def media(self):
        media_matematica = (self.prova_1_notas['matematica'] + self.prova_2_notas['matematica']) / 2
        media_portugues = (self.prova_1_notas['portugues'] + self.prova_2_notas['portugues']) / 2
        media_historia = (self.prova_1_notas['historia'] + self.prova_2_notas['historia']) / 2
        media_geografia = (self.prova_1_notas['geografia'] + self.prova_2_notas['geografia']) / 2

        self.mediaProvas = {
            "Matematica_media": media_matematica,
            "Portugues_media": media_portugues,
            "Historia_media": media_historia,
            "Geografia_media": media_geografia
        }
        return self.mediaProvas

provaInstance = prova(prova1, prova2)
print(provaInstance.media())



def calculadora():
    listOperators = ["soma", "subtracao", "divisao", "multiplicacao"]
    while True:
     try:
        num1 = int(input("Digite o primeiro número: "))
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")
    
    while True:
     try:
        num2 = int(input("Digite o segundo número: "))
        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")

    while True:
     operatorType = str(input("Digite um dos tipos de operação: soma, subtracao, divisao ou multiplicacao (!!SEM ACENTOS!!)"))
     if operatorType in listOperators:
        break
     print("Valor inválido! Digite apenas: soma, subtracao, divisao ou multiplicacao.")
    
    result = 0
    if (operatorType == "soma"):
        result = num1 + num2
    if(operatorType == "subtracao"):
        result = num1 - num2
    if(operatorType == "divisao"):
        result = num1 / num2
    if(operatorType == "multiplicacao"):
        result = num1 * num2

    print(int(result))


#calculadora()