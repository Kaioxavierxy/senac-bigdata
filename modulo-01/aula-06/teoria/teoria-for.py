#             inicio, final, gap
for i in range(1, 10, 2):
    print(i)

for i in range(5):  
 try: 
 # i representa o número atual da repetição (0, 1, 2...) 
  print(f"Número {i + 1} de 5:") 
  num = float(input("Digite um número: ")) 
  dobro = num * 2 
  triplo = num * 3 
  quádruplo = num * 4 
  print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n") 
 except ValueError: 
  print("Entrada inválida. Tente novamente.")


limite = 0

while True: # Loop infinito garantido para executar pelo menos uma vez 
 if contador >= limite: 
  break # Ponto de DECISÃO: Se o limite for atingido, usamos 'break' para sair 
 try: 
   print(f"Número {contador + 1} de {limite}:") 
   num = float(input("Digite um número: ")) 
   dobro = num * 2 
   triplo = num * 3 
   quádruplo = num * 4 
   print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n") 
   contador = contador + 1 # Incremento 
 except ValueError: 
  print("Entrada inválida. Tente novamente.")