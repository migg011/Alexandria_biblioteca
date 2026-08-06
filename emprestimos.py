def realizar_emprestimo():
    cod_usuario = int(input("Código do usuario: "))
    cod_livro = int(input("Código do livro:"))  # Corrigido

    usuario = buscar_usuario(cod_usuario)
    livro = buscar_livro(cod_livro)

    emprestimos.append({
        "usuario": usuario,
        "livro": livro
    })

    livro["quantidade"] -= 1

    print("Emprestimo realizado")