def ler_inteiro(mensagem, min_val=None, max_val=None):
    # Lê um número inteiro de forma segura (feito no Commit 1)
    pass


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