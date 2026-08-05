from usuarios import buscar_usuario
from livros import buscar_livro

emprestimos = []

def realizar_emprestimo():
    cod_usuario = int(input("Código do usuario: "))
    cod_livro = int(input("Código do livro:" )

    usuario = buscar_usuario(cod_usuario)
    livro = buscar_livro(cod_livro)

    emprestimos.append({
        "usuario": usuario,
        "livro": livro
    })

    livro ["quantidade"] -= 1

    print("Emprestimo realizado")