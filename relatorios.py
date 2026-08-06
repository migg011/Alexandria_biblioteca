from emprestimos import  realizar_emprestimo

def registrar_devolucao(self, id_emprestimo: int) -> str:
    emprestimo = realizar_emprestimo()[id_emprestimo]

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
    total_titulos =len(self.titulos)
    total_exemplars =len(self.acervo)

    disponivel = sum(1 for ex  in self.acervo.value() if ex['status'] == 'disponivel')
    emprestimos = sum(1 for ex in self.acervo.value() if ex['status'] ==  'emprestado')

    relatorio = {
        'total_titulos': total_titulos,
        'total_exemplars': total_exemplars,
        'disponivel': disponivel,
        'emprestimos': emprestimos,
    }
    return relatorio

def imprimir_relatorio(self):

    dados = self.gerar_relatorio_totais()
    print("-" * 40 )

    print("RELATORIO DE STATUS  DO ACERVO")
    print("-" * 40 )
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    print("-" * 40 )