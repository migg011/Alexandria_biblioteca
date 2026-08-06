def exibir_menu():
    print("=" * 36)
    print("         SISTEMA DE BIBLIOTECA")
    print("=" * 36)
    # opcoes do menu
    print("0 - Sair")
    print("7 - Histórico do usuário")
    print("=" * 36)


def ler_opcao():
    try:
        entrada = input("Escolha uma opção: ").strip()
        if not entrada:
            raise ValueError("A entrada não pode ser vazia.")
        return int(entrada)
    except ValueError:
        return None