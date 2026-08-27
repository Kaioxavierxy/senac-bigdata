livro = {
 'titulo': 'Dom Quixote',
 'autor': 'Cervantes',
 'ano': 1605,
 'preço': 27.90
};

print(f"Dicionário Original: {livro}");

titulo_livro = livro['titulo']  ## Acessando a chave titulo do objeto livro
print(f"O livro é: {titulo_livro}")

livro['editora'] = 'L&PM' ## Inclusão

livro.pop('ano')