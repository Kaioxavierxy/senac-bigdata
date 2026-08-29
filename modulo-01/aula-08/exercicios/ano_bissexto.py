# 1. Verificador de Ano Bissexto
# Crie uma função chamada eh_bissexto(ano):
# ● A função deve receber um ano (inteiro) como parâmetro.
# ● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
# ● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
# menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
# e 2100 não são).
# ● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
# "O ano X NÃO é bissexto", baseado no retorno da função.
# 55, 123, 1.002, 5.550.
 
an02 = 2100
anon = an02 % 400
anon2 = an02 % 100
print (anon, anon2)


def eh_bissexto(ano): 
    control = False

    if(ano % 4 == 0):
        control = True

    if(ano % 100 == 0):
        control = False

    if(ano % 100 == 0 and ano % 400 == 0):
        control = True

    return control

print(eh_bissexto(2000))
