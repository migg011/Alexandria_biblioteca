usuarios = []


def cadastrar_usuario():
    codigo = int(input("Código: "))
    nome = input("Nome: ")

    usuarios.append({
        "codigo": codigo,
        "nome": nome
    })

def buscar_usuario(codigo):
    for usuario in usuarios:
        if usuario["codigo"] == codigo:
            return usuario

    return None