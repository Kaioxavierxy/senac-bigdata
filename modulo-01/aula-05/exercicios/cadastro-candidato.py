lista_usuarios = []


while True:
    contador = 0

    if(contador >  12):
        break

    ano_nascimento = int(input("Insira o seu ano de nascimento: "))
    idade = 2026 - ano_nascimento
    
    
    if(idade < 18):
      print("Você não é maior de idade! Looping encerrado")
      print("Lista atual: ", lista_usuarios)
      break

    nome = str(input("Insira o seu nome: "))
    email = str(input("Insira o seu email: "))

    lista_usuarios.append(
        {
            "nome": nome,
            "idade": idade,
            "email": email
        }
    )

    contador += 1
    print("Usuário cadastrado com sucesso! Redirecionando para novo cadastro...")
   