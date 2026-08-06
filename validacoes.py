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
    """Lê uma string obrigatória, sem aceitar vazios ou apenas espaços em branco."""
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("Erro: O campo não pode ficar vazio. Tente novamente.")


def pedir_confirmacao(mensagem):
    """Pede confirmação do tipo Sim/Não. Retorna True para 's'/'sim' e False para 'n'/'não'."""
    while True:
        resposta = input(f"{mensagem} (S/N): ").strip().lower()
        if resposta in ["s", "sim"]:
            return True
        elif resposta in ["n", "nao", "não"]:
            return False
        print("Erro: Resposta inválida. Por favor, responda com 'S' para Sim ou 'N' para Não.")