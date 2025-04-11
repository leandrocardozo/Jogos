

import random
from time import sleep
import os
from funcoes_amigo import leia_int
from funcoes_amigo import leia_string
from funcoes_amigo import sorteio_valido


print('\033[1;3;92m  *********************')
print('  SORTEIO AMIGO SECRETO           ')
print('_________________________\033[m  ')


amigos = []

qnt_amigos = leia_int('\n\033[3mQuantos amigos irão participar: ')
print('---------------------------------')


## Cadastra o nome dos participantes de acordo com a quantidade declarada.
## Verifica se o input do usuário para cadastrar um amigo é válido.
for i in range(qnt_amigos):
    while True:
        amigo = str(input(f'Nome completo do {i+1}º amigo secreto: ')).lower().title()

        if amigo.isnumeric():
            print('\033[33mATENÇÃO! Somente nomes.\033[m')
            print('-----------------------')
        else:
            amigos.append(amigo)
            print(f'\033[1;3;33m- {amigo} cadastrado(a) com sucesso!\033[m')
            break
print('-----------------------------')


inicia_sorteio = leia_string('Deseja iniciar o sorteio? [S/N]')

if 'S' in inicia_sorteio:

    print('Você será redirecionado para a pagina do sorteio..')
    sleep(5)
    os.system('clear')

    print('\033[1;3;92m-------------------')
    print(' PAGINA DO SORTEIO ')
    print('-------------------\033[m')
    print(f'\nPARTICIPANTES:')
    for part, amigo_secreto in enumerate(amigos):
        print(f'{part + 1} - \033[3;33m{amigo_secreto}\033[m')

    sleep(2)
    print('\nSORTEANDO..')
    sleep(3)

    embaralhados = random.sample(amigos, len(amigos))
    while not sorteio_valido(amigos, embaralhados):
        embaralhados = random.sample(amigos, len(amigos))

    for i in range(len(amigos)):
        with open(f'{amigos[i]}.txt', 'w') as arquivo:
            arquivo.write(f'Você tirou: {embaralhados[i]}')


    print('-------------------')
    print('\033[1;3;31mSorteio finalizado!\033[m')
    print('\033[3;37mNota: Um arquivo .txt foi criado com seu nome contendo o seu amigo oculto!\033[m')
    print('\033[3;37mSeja discreto ;)\033[m')
elif 'N' in inicia_sorteio:
    print('Sorteio Cancelado!')
else:
    print('!!!ATENÇÃO!!!! Digite [S] ou [N].')
