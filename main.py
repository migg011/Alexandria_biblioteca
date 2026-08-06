from menu import exibir_menu, ler_opcao


def main():
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 0:
            print("Saindo do sistema...")
            break
        elif opcao == 7:
            print("[Módulo] Histórico do usuário selecionado.")
        elif opcao == -1:
            print("Erro: Digite apenas números inteiros!")
        else:
            print("Opção inválida ou ainda não integrada.")


if __name__ == "__main__":
    main()