usuario_banco = "kaio_senac";
senha_banco = "1234";

contador = int(3);

for i in range(3):
  usuario_input = str(input("Seu usuario: "));
  senha_input = str(input("Sua senha: "));

  if contador <= 1:
    print("Limite de tentativas excedito, tente novamente mais tarde.");
    break;

  if(usuario_input != usuario_banco or senha_input != senha_banco):
    contador -= 1;
    print("Usuário ou senha incorreto! Você tem mais ", contador, "tentativas");
    continue;

  print("Você entrou no sistema com sucesso!");
  break;