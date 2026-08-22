usuario_banco = "kaio_senac"
senha_banco = "1234"

contador = 3
logado = False

for i in range(3):
  if(contador == 0):
    print("limite de tentativas excedito, tente novamente mais tarde")
  if(logado):
    continue
  usuario_input = str(input("Seu usuario: "))
  senha_input = str(input("Sua senha: "))

  if(usuario_input != usuario_banco or senha_input != senha_banco):
    print("Usuário ou senha incorreto! Você tem mais ", i, "Tentativas")
    contador -= 1
    continue

  print("Você entrou no sistema com sucesso!")
  logado = True
  continue