def ler_inteiro(mensagem, min_val=None, max_val=None):
#Lê um número inteiro de forma segura. Trata erro se o usuário digitar algo que não seja número.
#Permite opcionalmente definir um valor mínimo e máximo (útil para opções do menu)

    while True:
        try:
            entrada = input(mensagem).strip()
            valor = int(entrada)

            if min_val is not None and valor < min_val:
                print(f"Erro: O valor deve ser no mínimo {min_val}.")
                continue

            if max_val is not None and valor > max_val:
                print(f"Erro: O valor deve ser no máximo {max_val}.")
                continue

            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro válido.")


def ler_texto(mensagem):
#Lê uma string obrigatória. Garante que o usuário não deixe o campo vazio ou apenas com espaços
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada inválida! Este campo não pode ficar em branco.")


def pedir_confirmacao(mensagem):
#Pede confirmação do tipo Sim/Não ao usuário.
#Retorna True para 'S' / 'Sim' e False para 'N' / 'Não'.

    while True:
        resposta = input(f"{mensagem} (S/N): ").strip().upper()
        if resposta in ['S', 'SIM']:
            return True
        elif resposta in ['N', 'NAO', 'NÃO']:
            return False
        else:
            print("Resposta inválida! Digite 'S' para Sim ou 'N' para Não.")