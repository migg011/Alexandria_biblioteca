def exibir_menu():
    print("=" * 36)
    print("         SISTEMA DE BIBLIOTECA")
    print("=" * 36)
    print("0 - Sair")
    print("1 - Cadastrar livro")
    print("2 - Listar e buscar livros")
    print("3 - Cadastrar usuário")
    print("4 - Realizar empréstimo")
    print("5 - Realizar devolucao")
    print("6 - Exibir relatorios")
    print("7 - Listar usuários")
    print("=" * 36)


def ler_opcao():
    try:
        entrada = input("Escolha uma opção: ").strip()
        if not entrada:
            raise ValueError("A entrada não pode ser vazia.")
        return int(entrada)
    except ValueError:
        return None