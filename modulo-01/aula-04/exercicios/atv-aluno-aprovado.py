nota_1 = int(input("insira a primeira nota: "))
nota_2 = int(input("insira a segunda nota: "))
optativa = str(input("Você fez a prova optativa? (sim/nao): "))

if(optativa == "sim"):
  nota_optativa = int(input("insira a nota da disciplina optativa: "))
  if(nota_optativa != -1 and nota_optativa > nota_2):
   nota_2 = nota_optativa
else: 
  nota_optativa = -1

print(nota_1, nota_2, nota_optativa)

media = float((nota_1 + nota_2) / 2)

if media < 3:
    status = "Reprovado"
    
elif media >= 3 and media <= 6:
    status = "Recuperação"

elif media >= 6 and media <= 10:
    status = "Aprovado"

print(status)
