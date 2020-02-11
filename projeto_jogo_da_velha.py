from random import randint
from time import sleep
from random import choice

#humano = 0
escolha1 =0
jogada = 1
tabuleiro_inicial = '''
--- COMO JOGAR ---
Quando for sua vez, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
Por exemplo, digamos que você queira jogar no centro, então você digita 5.
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''
print(tabuleiro_inicial)
print(input('\033[1;31m Aperte o enter para continuar\033[m'))
print('=-=' *25)
print('=-=' *25)
print(' \n')



table = [1 ,2 ,3 ,4 ,5 , 6, 7, 8, 9]

def desenha_tabuleiro():
    print('\n')
    print('==='*10)
    print('\n')
    print(f'       {table[0]}   |   {table[1]}   |   {table[2]}')
    print(f'           |       |      ')
    print('     --------------------')
    print(f'       {table[3]}   |   {table[4]}   |   {table[5]}')
    print(f'           |       |      ')
    print('     --------------------')
    print(f'       {table[6]}   |   {table[7]}   |   {table[8]}')
    print(f'           |       |      ')
    print('\n')
    print('===' * 10)


#def xis_ou_bola():

humano = 'X'
maquina = 'O'


print('=-=' *25)
print('=-=' *25)
print(' \n')

def vencedor():
    global table
    for i in ['X', 'O']:
        # horizontal
        if table[0] == table[1] == table[2] == i: return i
        if table[3] == table[4] == table[5] == i: return i
        if table[6] == table[7] == table[8] == i: return i
        # vertical
        if table[0] == table[3] == table[6] == i: return i
        if table[1] == table[4] == table[7] == i: return i
        if table[2] == table[5] == table[8] == i: return i
        # diagonal
        if table[0] == table[4] == table[8] == i: return i
        if table[6] == table[4] == table[2] == i: return i
        # empate

    return None

def fulltable():
    global table
    if table == [humano , maquina]:
        return True




def cleartable():
    global table
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = '1', '2', '3', '4', '5', '6', '7', '8', '9'
    table = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

def move(pos):
    global jogada
    global table

    if not pos: return None
    if not 0 < pos < 10: return False
    if table[pos - 1] in ['X', 'O']: return False
    table[pos - 1] = ('O', 'X')[jogada == 1]
    jogada = (1, 2)[jogada == 1]
    sleep(0.3)

placarhumano = 0
placarmaquina =0
empates = 0
while True:

    print(f'Player {jogada}')
    if jogada == 1:
        movement = int(input('1-9:'))
        sleep(0.3)
    if jogada == 2:
        movement = int(input('1-9:'))

        #movement = randint(1,10)


    move(movement)
    desenha_tabuleiro()
    win = vencedor()
    empate = fulltable()

    if empate:
        print('Houve um empate')
        empates += 1
        print(f'|Humano {placarhumano}, maquina {placarmaquina}, empates {empates}|')
        continuar = input('\033[1;34mDeseja continuar, S ou N\033[m'.lower())
        if continuar == 's':
            cleartable()
            continue
        if continuar == 'n':
            exit()

    if not win: continue
    print('===' * 11)
    print('\033[1;93m|PLACAR ATUAL|\033[m')
    print('===' * 11)
    if win == humano:
        print("Player 1 Wins!" )
        placarhumano += 1
        print(f'|Humano {placarhumano}, maquina {placarmaquina}, empates {empates}|')
        continuar = input('\033[1;34mDeseja continuar, S ou N\033[m'.lower())
        if continuar == 's':
            cleartable()
            continue
        if continuar == 'n':
            exit()
    if win == maquina:
        print("Player 2 Wins!")
        placarmaquina += 1
        print(f'|Humano {placarhumano}, maquina {placarmaquina}, empates {empates}|')
        continuar = input('\033[1;34mDeseja continuar, S ou N\033[m'.lower())
        if continuar == 's':
            cleartable()
            continue
        if continuar == 'n':
            exit()
    if empate:
            print('Houve um empate')
            empates +=1
            print(f'|Humano {placarhumano}, maquina {placarmaquina}, empates {empates}|')
            continuar = input('\033[1;34mDeseja continuar, S ou N\033[m'.lower())
            if continuar == 's':
                cleartable()
                continue
            if continuar == 'n':
                exit()

desenha_tabuleiro()
print('=-=' *25)
print('=-=' *25)
print(' \n')

