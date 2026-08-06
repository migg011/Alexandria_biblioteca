# Lógica de cadastro
def cadastrar_livro(acervo, codigo, titulo, autor, quantidade):
    for livro in acervo:
        if livro['codigo'] == codigo:
            return False

    if not titulo or titulo.strip() == "":
        return False

    if quantidade <= 0:
        return False

    novo_livro = {
        'codigo': codigo,
        'titulo': titulo.strip(),
        'autor': autor.strip(),
        'quantidade': quantidade
    }
    acervo.append(novo_livro)
    return True

# Lógica de edição
def editar_livro(acervo, codigo, novo_titulo=None, novo_autor=None, nova_quantidade=None):
    livro_encontrado = None
    for livro in acervo:
        if livro['codigo'] == codigo:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        return False

    if novo_titulo is not None:
        if novo_titulo.strip() == "":
            return False
        livro_encontrado['titulo'] = novo_titulo.strip()

    if novo_autor is not None:
        livro_encontrado['autor'] = novo_autor.strip()

    if nova_quantidade is not None:
        if nova_quantidade <= 0:
            return False
        livro_encontrado['quantidade'] = nova_quantidade

    return True

# Lógica de remoção
def remover_livro(acervo, codigo):
    for i, livro in enumerate(acervo):
        if livro['codigo'] == codigo:
            acervo.pop(i)
            return True
    return False

# Lógica de listagem
def listar_livros(acervo):
    for livro in acervo:
        print(livro)