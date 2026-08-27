numeros = {10, 20, 30, 10, 40, 30}
print(f"Set Original: {numeros}")

numeros.add(10) # Será ignorado, pois 10 já existe

## Verificação se o número está presente na lista
if 20 in numeros:
 print("O número 20 está no conjunto.")


numeros.remove(40)
print(f"Set após remover 40: {numeros}")