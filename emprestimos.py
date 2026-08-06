# Importar a função correta do módulo consultas
from consultas import buscar_por_codigo


def realizar_emprestimo(cod_usuario, cod_livro, usuarios, livros, emprestimos):
    # 1. Busca os registros
    usuario = buscar_por_codigo(cod_usuario)  # Ajuste conforme a função de busca de usuário usada no projeto
    livro = buscar_por_codigo(cod_livro)  # CORREÇÃO 1: Utiliza buscar_por_codigo em vez de listar_livros

    # 2. CORREÇÃO 2: Validações de None no INÍCIO, antes de acessar propriedades
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return False

    if livro is None:
        print("Erro: Livro não encontrado.")
        return False

    # 3. Acesso seguro às chaves do dicionário somente após confirmar que não é None
    if livro["quantidade"] <= 0:
        print("Erro: Não há exemplares disponíveis deste livro.")
        return False

    # Lógica de registro do empréstimo...
    livro["quantidade"] -= 1
    # ... adiciona ao dicionário/lista de empréstimos ...

    print("Empréstimo realizado com sucesso!")
    return True