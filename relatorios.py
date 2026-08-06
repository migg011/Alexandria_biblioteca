from Alexandria_biblioteca.emprestimos import emprestimos


def registrar_devolucao(self, id_emprestimo: int) -> str:
    emprestimo = emprestimos[id_emprestimo]

    if not emprestimo:
        raise ValueError("emprestimo nao encontrado")

    if emprestimo.get('devolvido'):
        raise ValueError("ERRO: Este Exemplar ja foi devolvido anteriormente")


def relatorio():
    pass