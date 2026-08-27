pessoas = [
    {
        "Nome": "Kaio",
        "idade": 22
    },
    {
        "Nome": "julia",
        "idade": 15
    },
    {
        "Nome": "Luiz",
        "idade": 54
    },
    {
        "Nome": "vitor",
        "idade": 17
    },
    {
        "Nome": "roberta",
        "idade": 16
    },
    {
        "Nome": "raquel",
        "idade": 21
    },    
]

pessoas_valias = []
pessoas_invalidas = []

for i in pessoas:
   if(i["idade"] < 18):
    nome = i["Nome"]
    pessoas_invalidas.append(i["Nome"])
   else:
    pessoas_valias.append(
        i
    ) 

print(pessoas_invalidas)
print(pessoas_valias)


