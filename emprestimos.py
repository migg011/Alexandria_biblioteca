from usuarios import buscar_usuario
from livros import listar_livros

def realizar_emprestimo():
    cod_usuario = int(input("Código do usuario: "))
    cod_livro = int(input("Código do livro:"))  # Corrigido

    usuario = buscar_usuario(cod_usuario)
    livro =listar_livros(cod_livro)

    if livro is None:
        print("Livro não encontrado.")
        return

    if livro["quantidade"] <= 0:
        print("Livro indisponível para empréstimo.")
        return

    emprestimos.append({
        "usuario": usuario,
        "livro": livro
    })

    livro["quantidade"] -= 1

    if usuario is None:
        print("Usuário não encontrado.")
        return

    if livro is None:
        print("Livro não encontrado.")
        return

    print("Emprestimo realizado")

