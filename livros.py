# Lógica de cadastro
def cadastrar_livro(acervo, codigo, titulo, autor, quantidade):
    for livro in acervo:
        if livro['codigo'] == codigo:
            return

    if not titulo or titulo.strip() == "":
        return

    if quantidade <= 0:
        return

    novo_livro = {
        'codigo': codigo,
        'titulo': titulo,
        'autor': autor,
        'quantidade': quantidade
    }
    acervo.append(novo_livro)

# Lógica de edição
def editar_livro(acervo, codigo, novo_titulo=None, novo_autor=None, nova_quantidade=None):
    for livro in acervo:
        if livro['codigo'] == codigo:
            if novo_titulo is not None:
                if novo_titulo.strip() == "":
                    return
                livro['titulo'] = novo_titulo.strip()

            if novo_autor is not None:
                livro['autor'] = novo_autor.strip()

            if nova_quantidade is not None:
                if nova_quantidade <= 0:
                    return
                livro['quantidade'] = nova_quantidade

# Lógica de remoção
def remover_livro(acervo, codigo):
    for i, livro in enumerate(acervo):
        if livro['codigo'] == codigo:
            acervo.pop(i)

# Lógica de listagem
def listar_livros(acervo):
    for livro in acervo:
        print(livro)