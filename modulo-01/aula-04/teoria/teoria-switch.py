mes = int(input("Informe o mês de seu nascimento:"))
 #VISÃO MATH CASE:
match mes: 
    case 1:
        signo = "Aquário"
    case 2:
        signo = "Peixes"
    case 3:
        signo = "Áries"
    case 4:
        signo = "Touro"
    case 5:
        signo = "Gêmeos"
    case 6:
        signo = "Câncer"
    case 7:
        signo = "Leão"
    case 8:
        signo = "Virgem"
    case 9:
        signo = "Libra"
    case 10:
        signo = "Escorpião"
    case 11:
        signo = "Sagitário"
    case 12:
        signo = "Capricórnio"

print(signo)
