codigo = int(input("Insira o código do produto"))

if codigo == 1:
    resultado = "Sul"
elif codigo == 2:
    resultado = "Norte"
elif codigo == 3:
    resultado = "Leste"
elif codigo == 4: 
    resultado = "Oeste"
elif codigo == 5 or codigo == 6:
    resultado = "Nordeste"
elif codigo == 7 or codigo == 8 or codigo == 9:
    resultado = "Sudeste"
elif codigo == 10:
    resultado = "Centro-Oeste"
elif codigo == 11:
    resultado = "Noroeste"
else: 
    resultado = "importado"

print(resultado)