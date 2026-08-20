numero = int(input("Escolha um número: "))

def verificaNumero(n):
    if n < 0: 
        resultado = "negativo";
    
    if n >= 0: 
        resultado = "postivo"

    print(resultado)

verificaNumero(numero);
