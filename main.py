from menu import exibir_menu, ler_opcao

# Importações ajustadas (somente funções utilizadas)
from consultas import buscar_por_titulo_parcial
from emprestimos import realizar_emprestimo
from livros import cadastrar_livro, listar_livros
from relatorios import registrar_devolucao, imprimir_relatorio
from usuarios import cadastrar_usuario, listar_usuarios
from validacoes import ler_texto


def main():
    """Ponto de entrada do sistema. Controla o laço principal e a integração das rotas."""
    acervo = []
    usuarios_lista = []
    emprestimos = []
    titulos_dict = {}

    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao is None:
            print("[Aviso] Entrada inválida. Digite apenas o número de uma das opções.")
            continue

        if opcao == 0:
            print("Encerrando o sistema da biblioteca. Até logo!")
            break

        elif opcao == 1:
            # Cadastrar livro
            print("\n--- Cadastrar Novo Livro ---")
            codigo = ler_texto("Código do livro: ")
            titulo = ler_texto("Título do livro: ")
            autor = ler_texto("Autor do livro: ")
            try:
                quantidade = int(ler_texto("Quantidade de exemplares: "))
                cadastrar_livro(acervo, codigo, titulo, autor, quantidade)
                titulos_dict[codigo] = titulo
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro válido.")

        elif opcao == 2:
            # Listar e buscar livros
            print("\n--- Consultar Acervo ---")
            print("1 - Listar todos os livros")
            print("2 - Buscar por termo no título")
            sub_opcao = input("Escolha uma opção (1 ou 2): ").strip()

            if sub_opcao == "1":
                listar_livros(acervo)
            elif sub_opcao == "2":
                termo = ler_texto("Digite o termo de busca: ")
                resultados = buscar_por_titulo_parcial(acervo, termo)
                if resultados:
                    for livro in resultados:
                        cod = str(livro.get('codigo') or '')
                        tit = str(livro.get('titulo') or '')
                        aut = str(livro.get('autor') or '')
                        qtd = str(livro.get('quantidade') or 0)
                        print(f"Código: {cod} | Título: {tit} | Autor: {aut} | Qtd: {qtd}")
                else:
                    print("Nenhum livro encontrado com esse termo.")
            else:
                print("Opção de busca inválida.")

        elif opcao == 3:
            # Cadastrar usuário
            print("\n--- Cadastrar Usuário ---")
            cadastrar_usuario()

        elif opcao == 4:
            # Realizar empréstimo
            print("\n--- Realizar Empréstimo ---")
            cod_usuario = ler_texto("Código do usuário: ")
            cod_livro = ler_texto("Código do livro: ")
            realizar_emprestimo(cod_usuario, cod_livro, usuarios_lista, acervo, emprestimos)

        elif opcao == 5:
            # Realizar devolução
            print("\n--- Realizar Devolução ---")
            try:
                id_emp = int(ler_texto("ID do Empréstimo: "))
                # Converte o acervo (list) em dict para atender a assinatura do módulo relatorios
                acervo_dict = {str(livro['codigo']): livro for livro in acervo}
                resultado = registrar_devolucao(id_emp, acervo_dict)
                print(resultado)
            except ValueError as e:
                print(f"[Erro] {e}")

        elif opcao == 6:
            # Exibir relatórios
            print("\n--- Relatório Geral ---")
            acervo_dict = {str(livro['codigo']): livro for livro in acervo}
            imprimir_relatorio(titulos_dict, acervo_dict)

        elif opcao == 7:
            # Histórico/Listagem de Usuários
            print("\n--- Lista de Usuários ---")
            listar_usuarios()

        else:
            print(f"[Aviso] A opção {opcao} é inválida. Escolha um número entre 0 e 7.")


if __name__ == "__main__":
    main()