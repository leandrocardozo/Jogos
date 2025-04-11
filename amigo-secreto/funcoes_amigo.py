

def leia_int(msg):
    """
    Função que verifica se o input do usuário é do tipo inteiro.
    :param msg: Uma mensagem que será exibida ao usuário pedindo um
    número do tipo inteiro.
    :return: Um número inteiro.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mATENÇÃO! Somente números!\033[m')
        else:
            return n


def leia_string(msg):
    """
    Função que permite somente caracteres e invalida se o usuário digitar
    números inteiros.
    :param msg: Somente caracteres
    :return: Um ou mais caracteres
    """
    while True:
        a = str(input(msg)).upper()
        if a.isnumeric():
            print('\033[33mATENÇÃO! Digite S ou N.\033[m')
            print('-----------------------')
        else:
            return a
            break


def sorteio_valido(amigos, embaralhados):
    """
    Função que verifica se o sorteio é válido. Se o sorteante não tirou ele mesmo.
    :param amigos: Uma lista com os participantes do amigo oculto.
    :param embaralhados: Uma lista com os mesmos participantes embaralhados.
    :return: Um valor booleano de True se o sorteio for valido e False senão for válido.
    """
    for i in range(len(amigos)):
        if amigos[i] == embaralhados[i]:
            return False
    return True
