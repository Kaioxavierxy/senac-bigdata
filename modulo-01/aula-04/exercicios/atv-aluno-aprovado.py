aluno_notas = {
    "matematica_1b": 6,
    "matematica_2b": 8,
    "matematica_3b": 5,
    "matematica_4b": 10,
}

def Aprovado(lista: list):
   n = 0
   status = "status inicial"

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