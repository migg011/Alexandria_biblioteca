def exibir_menu():
    """Exibe no console o cabeçalho e as opções disponíveis do sistema."""
    print("=" * 36)
    print("         SISTEMA DE BIBLIOTECA")
    print("=" * 36)
    # opcoes do menu
    print("0 - Sair")
    print("1 - Cadastrar livro")
    print("2 - Listar e buscar livros")
    print("3 - Cadastrar usuário")
    print("4 - Realizar empréstimo")
    print("5 - Realizar devolucao")
    print("6 - Exibir relatorios")
    print("7 - Histórico do usuário")
    print("=" * 36)


def ler_opcao():
    """Lê a entrada do usuário, remove espaços e valida se é um número inteiro.

    Retorna o valor convertido em int ou None caso a entrada seja inválida.
    """
    try:
        entrada = input("Escolha uma opção: ").strip()
        if not entrada:
            raise ValueError("A entrada não pode ser vazia.")
        return int(entrada)
    except ValueError:
        return None