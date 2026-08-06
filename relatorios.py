from Alexandria_biblioteca.emprestimos import emprestimos


def registrar_devolucao(self, id_emprestimo: int) -> str:
    emprestimo = emprestimos[id_emprestimo]

    if not emprestimo:
        raise ValueError("emprestimo nao encontrado")

    if emprestimo.get('devolvido'):
        raise ValueError("ERRO: Este Exemplar ja foi devolvido anteriormente")

    emprestimo['devolvido'] = True
    id_exemplar = emprestimo['id_exemplar']
    if id_exemplar in self.acervo:
        self.acervo[id_exemplar]['status'] = 'disponivel'
        return f'Sucesso: O exemplar {id_exemplar} foi devolvido'
    else:
        raise ValueError("ERRO: O exemplar associado a este  emprestimo nao existe no acervo ")



def gerar_relatorio_totais(self):
    pass

def relatorio():
    pass