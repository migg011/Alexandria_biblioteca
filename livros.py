# Lógica de cadastro
def cadastrar_livro(acervo, codigo, titulo, autor, quantidade):
#Cadastra um novo livro no acervo apos validar os dados fornecidos
    for livro in acervo:
        if livro['codigo'] == codigo:
            print(f"Erro: O código '{codigo}' já está cadastrado.")
            return False

    if not titulo or titulo.strip() == "":
        print("Erro: O título do livro não pode ser vazio.")
        return False

    if quantidade <= 0:
        print("Erro: A quantidade deve ser um número maior que zero.")
        return False

    novo_livro = {
        'codigo': codigo,
        'titulo': titulo.strip(),
        'autor': autor.strip(),
        'quantidade': quantidade
    }
    acervo.append(novo_livro)
    print(f"Sucesso: Livro '{titulo}' cadastrado com sucesso!")
    return True

# Lógica de edição
def editar_livro(acervo, codigo, novo_titulo=None, novo_autor=None, nova_quantidade=None):
#Edita informacoes de um livro cadastrado no acervo
    livro_encontrado = None
    for livro in acervo:
        if livro['codigo'] == codigo:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        print(f"Erro: Livro com código '{codigo}' não foi encontrado.")
        return False

    if novo_titulo is not None:
        if novo_titulo.strip() == "":
            print("Erro: O título não pode ser alterado para um valor vazio.")
            return False
        livro_encontrado['titulo'] = novo_titulo.strip()

    if novo_autor is not None:
        livro_encontrado['autor'] = novo_autor.strip()

    if nova_quantidade is not None:
        if nova_quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return False
        livro_encontrado['quantidade'] = nova_quantidade

    print(f"Sucesso: Dados do livro com código '{codigo}' atualizados.")
    return True

# Lógica de remoção
def remover_livro(acervo, codigo):
#Remove um livro do acervo utilizando o código
    for i, livro in enumerate(acervo):
        if livro['codigo'] == codigo:
            livro_removido = acervo.pop(i)
            print(f"Sucesso: Livro '{livro_removido['titulo']}' removido do acervo.")
            return True

    print(f"Erro: Livro com código '{codigo}' não encontrado para remoção.")
    return False

# Lógica de listagem
def listar_livros(acervo):
    if not acervo:
        return False

    for livro in acervo:
        print(livro)
    return True