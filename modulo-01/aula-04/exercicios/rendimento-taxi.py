km_inicial = int(input("Escolha o km inicial do trajeto: "))
km_final = int(input("Escolha o km km_final do trajeto: "))
km_litro = int(input("Quantos litros percorridos por km: "))

VALOR_GASOLINA = 6.15

percurso = km_final - km_inicial
km_litro_gastos = percurso / km_litro
valor_gasto = km_litro_gastos * 6.15

print("Percurso percorrido: ", percurso)
print("Litros gastos: ", km_litro_gastos)
print("Valor gasto com combustivel: ", valor_gasto)