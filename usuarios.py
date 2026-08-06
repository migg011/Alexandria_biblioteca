usuarios = []


def cadastrar_usuario():
    codigo = int(input("Código: "))

    if buscar_usuario(codigo):
        print("Código já cadastrado.")
        return

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

