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
    pass

# Lógica de remoção...
def remover_livro(acervo, codigo):
    pass

# Lógica de listagem...
def listar_livros(acervo):
    pass