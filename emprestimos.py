from consultas import buscar_por_codigo
from usuarios import buscar_usuario


def realizar_emprestimo(cod_usuario, cod_livro, usuarios, livros, emprestimos):
    # 1. Busca os registros passando os parâmetros necessários
    try:
        cod_usr_num = int(cod_usuario)
    except ValueError:
        cod_usr_num = cod_usuario

    usuario = buscar_usuario(cod_usr_num)
    livro = buscar_por_codigo(livros, cod_livro)

    # 2. Validações de existência dos registros
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return False

    if livro is None:
        print("Erro: Livro não encontrado.")
        return False

    # 3. Acesso seguro à quantidade disponível
    if livro.get("quantidade", 0) <= 0:
        print("Erro: Não há exemplares disponíveis deste livro.")
        return False

    # 4. Atualização do acervo e registro do empréstimo
    livro["quantidade"] -= 1

    novo_emprestimo = {
        "id": len(emprestimos) + 1,
        "cod_usuario": cod_usuario,
        "cod_livro": cod_livro,
        "devolvido": False
    }
    emprestimos.append(novo_emprestimo)

    print(f"Sucesso: Empréstimo do livro '{livro.get('titulo')}' realizado para {usuario.get('nome')}!")
    return True