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


from random import randint
from time import sleep


lista_valor = []

# While principal que executa todo o programa mais de uma vez caso o usuário queira.
while True:

    jogo = []
    print('-----------------')
    print('    \033[33:1mMEGA SENA\033[m')
    print('-----------------')


    qnt_jogos = leia_int('Quantidade JOGOS: ')
    while True:

        qnt_num = str(input('Quantidade NÚMEROS: '))
        if qnt_num.isnumeric():
            pass
        else:
            print('\033[33mATENÇÃO! Somente números!\033[m')
            continue


        # Estrutura condicional que verifica o valor das apostas.
        # - Variável (qnt_num) é atribuida a quantidade de números que o usuário escolheu para o seu jogo.
        if int(qnt_num) == 6:
            valor_tot = qnt_jogos * 4.50
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 7:
            valor_tot = qnt_jogos * 31.50
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 8:
            valor_tot = qnt_jogos * 126.00
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 9:
            valor_tot = qnt_jogos * 378.00
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 10:
            valor_tot = qnt_jogos * 945.00
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 11:
            valor_tot = qnt_jogos * 2.079
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 12:
            valor_tot = qnt_jogos * 4.158
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 13:
            valor_tot = qnt_jogos * 7.722
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 14:
            valor_tot = qnt_jogos * 13.513
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.2f}\033[m')
            lista_valor.append(valor_tot)
        if int(qnt_num) == 15:
            valor_tot = qnt_jogos * 22.522
            print(f'\033[35mO valor total da sua aposta é: \033[m \033[33:1mR$ {valor_tot:.3f}\033[m')
            lista_valor.append(valor_tot)


        # Verifica o intervalo válido da quantidade de números permitidos na Mega Sena.
        if int(qnt_num) < 6 or int(qnt_num) > 15:
            print(' - Mín 6 dezenas e Máx 15 dezenas.')
        else:
            break

    # Um loop "for" que executa a quantidade de jogos selecionada pelo usuário.
    j = 0
    for j in range(qnt_jogos):

        jogo = []
        print(f'\nJogo {j+1}:')
        n = 0
        # Estrutura de criação e escritura de arquivo para relatório dos jogos.
        with open('megasena_jogos.txt', 'a+') as arquivo:
            arquivo.write(f'Jogo de {qnt_num} números.\n')


            # Estrutura lógica responsável pelo sorteio dos jogos.
            while n < int(qnt_num):
                a = randint(1, 60)
                if a not in jogo:
                    arquivo.write(f'{n+1}ª dezena: ' + str(a) + '\n')
                    jogo.append(a)
                    sleep(0.5)
                    print(f'\033[32:1m{a}\033[m', end=' ')
                    n += 1
            arquivo.write('-' * 19 + '\n')
        j += 1


    if j > 1:
        print('\nApostas encerradas!')
    else:
        print('\nAposta encerrada!')


    ## Pergunta ao usuário se ele deseja efetuar mais jogos
    while True:
        option = str(input('Deseja fazer mais jogos? [S/N]')).upper()
        if option not in 'SN':
            print('Digite S ou N.')
            continue
        else:
            break

    if option in 'S':
        continue
    else:
        print('\n-------------------------------')
        print(f'\033[36mTotal a pagar: \033[m \033[31:1mR$ {sum(lista_valor):.2f}\033[m')
        print('\033[37:3mO relatório de todos jogos estão no arquivo megasena_jogos.txt')
        print('Programa de apostas finalizado!')
        break
