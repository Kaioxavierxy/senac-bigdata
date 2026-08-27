lista_usuarios = []


while True:
    contador = 0
    if(contador >  12):
        break
  
  ## Condição bananada de verificação de input
    while True:
     try:
        ano_nascimento = int(input("Insira o seu ano de nascimento: "))
        idade = 2026 - ano_nascimento

        if(idade < 18):
           print("Você não é maior de idade! Looping encerrado")
           print("Lista atual: ", lista_usuarios)
           break

        break
     except ValueError:
        print("Erro! Digite um número inteiro válido.")
    
    nome = str(input("Insira o seu nome: "))
    email = str(input("Insira o seu email: "))

    usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
    }
    
    if usuario in lista_usuarios:
       print("Erro! O usuário já está registrado no banco de dados")
       print(f"Usuários cadastrados: {lista_usuarios}")
       break

    lista_usuarios.append(usuario)
    contador += 1
    print("Usuário cadastrado com sucesso! Redirecionando para novo cadastro...")
   