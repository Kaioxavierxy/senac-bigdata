aluno_notas = {
    "matematica_1b": 6,
    "matematica_2b": 1,
    "matematica_3b": 5,
    "matematica_4b": 1,
}

def Aprovado(lista: list):
   n = 0
   
   for i in lista:
     n += lista[i]
   
   n = n / len(lista)

   if n < 5:
    status = "Reprovado"
    
   elif n >= 5 and n <= 7:
    status = "Recuperação"

   elif n > 7 and n <= 10:
    status = "Aprovado"

   print(status)

Aprovado(lista=aluno_notas)