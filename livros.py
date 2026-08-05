# Lógica de cadastro...
def cadastrar_livro(acervo, codigo, titulo, autor, quantidade):
    novo_livro = {
        'codigo': codigo,
        'titulo': titulo,
        'autor': autor,
        'quantidade': quantidade
    }
    acervo.append(novo_livro)

# Lógica de edição...
def editar_livro(acervo, codigo, novo_titulo=None, novo_autor=None, nova_quantidade=None):
    for livro in acervo:
        if livro['codigo'] == codigo:
            if novo_titulo:
                livro['titulo'] = novo_titulo
            if novo_autor:
                livro['autor'] = novo_autor
            if nova_quantidade:
                livro['quantidade'] = nova_quantidade

# Lógica de remoção...
def remover_livro(acervo, codigo):
    for i, livro in enumerate(acervo):
        if livro['codigo'] == codigo:
            acervo.pop(i)

# Lógica de listagem...
def listar_livros(acervo):
    for livro in acervo:
        print(livro)