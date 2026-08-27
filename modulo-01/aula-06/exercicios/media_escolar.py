estudantes = [
    {
        "Nome": "Kaio",
        "matematica1": 8,
        "matematica2": 9
    },
    {
        "Nome": "julia",
        "matematica1": 4,
        "matematica2": 7
    },
    {
        "Nome": "Luiz",
        "matematica1": 10,
        "matematica2": 5
    },
    {
        "Nome": "vitor",
        "matematica1": 2,
        "matematica2": 5
    },
    {
        "Nome": "roberta",
        "matematica1": 3,
        "matematica2": 7
    },
    {
        "Nome": "raquel",
        "matematica1": 10,
        "matematica2": 8
    },    
]

def calcula_media(n1, n2):
    return float((n1 + n2) / 2)

resultado = []

for i in estudantes:
    media = calcula_media(i["matematica1"], i["matematica2"])
    nome = i["Nome"]

    if media < 3:
     status = f"{nome} - Está Reprovado"
     resultado.append(status)

    elif media >= 3 and media <= 6:
     status = f"{nome} - Está em Recuperação"
     resultado.append(status)

    elif media >= 6 and media <= 10:
     status = f"{nome} - Está Aprovado"
     resultado.append(status)

print(resultado)