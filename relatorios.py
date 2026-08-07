def registrar_devolucao(id_emprestimo: int, emprestimos: list, acervo: list) -> str:

    emprestimo_encontrado = None
    for emp in emprestimos:
        if emp.get("id") == id_emprestimo:
            emprestimo_encontrado = emp
            break


    if not emprestimo_encontrado:
        raise ValueError("Empréstimo não encontrado.")

    if emprestimo_encontrado.get("devolvido"):
        raise ValueError("ERRO: Este exemplar já foi devolvido anteriormente.")

    emprestimo_encontrado["devolvido"] = True
    cod_livro = emprestimo_encontrado.get("cod_livro")

    livro_encontrado = None
    for livro in acervo:
        if str(livro.get("codigo")) == str(cod_livro):
            livro["quantidade"] += 1
            livro_encontrado = livro
            break

    if livro_encontrado:
        return f"Sucesso: O exemplar '{livro_encontrado.get('titulo')}' foi devolvido e o estoque foi atualizado!"
    return f"Sucesso: Devolução registrada para o empréstimo #{id_emprestimo}."


def gerar_relatorio_totais(titulos: dict, acervo: list, emprestimos: list) -> dict:
    total_titulos = len(titulos)
    total_exemplares = sum(livro.get("quantidade", 0) for livro in acervo)
    total_emprestados = sum(1 for emp in emprestimos if not emp.get("devolvido", False))

    return {
        "Total de Títulos Cadastrados": total_titulos,
        "Total de Exemplares Disponíveis": total_exemplares,
        "Empréstimos Ativos": total_emprestados,
    }


def imprimir_relatorio(titulos: dict, acervo: list, emprestimos: list):

    dados = gerar_relatorio_totais(titulos, acervo, emprestimos)
    print("-" * 40)
    print("      RELATÓRIO DE STATUS DO ACERVO")
    print("-" * 40)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    print("-" * 40)

