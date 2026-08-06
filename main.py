from menu import exibir_menu, ler_opcao


def main():
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao is None:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")
            continue

        if opcao == 0:
            print("Saindo do sistema...")
            break
        elif opcao == 7:
            print("[Módulo] Histórico do usuário selecionado.")
        else:
            print(f"Opção {opcao} informada é inválida ou pendente de integração.")


if __name__ == "__main__":
    main()