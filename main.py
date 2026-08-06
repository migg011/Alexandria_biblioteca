from menu import exibir_menu, ler_opcao


def main():
    """Ponto de entrada do sistema. Controla o laço principal e o direcionamento das opções."""
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao is None:
            print("[Aviso] Entrada inválida. Digite apenas o número de uma das opções.")
            continue

        if opcao == 0:
            print("Encerrando o sistema da biblioteca. Até logo!")
            break
        elif opcao == 7:
            print("[Info] Módulo de histórico do usuário selecionado.")
        else:
            print(f"[Aviso] A opção {opcao} é inválida ou ainda não foi integrada pelos colegas.")


if __name__ == "__main__":
    main()