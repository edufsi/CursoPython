import random
from time import sleep
s = 0
titulo = 'JOGO DE PAR OU IMPAR'
while True:
    print(titulo.center(64))
    print('-' * 64)
    print('Máquina: par ou impar? ')
    x = str(input('Você: '))
    if x.upper() == 'PAR':
        print('Máquina: Impar')
        print('-' * 64)
    elif x.upper() == 'IMPAR':
        print('Máquina: Par')
        print('-' * 64)
    else:
        print('Máquina: Não entendi')
        break
    y = int(input('Digite 1 ou 2: '))
    if y != 1 and y != 2:
        print('Máquina: Não sabe jogar par ou impar? Só vale 1 e 2!')
        break
    z = int(random.randrange(1,3))
    print(f'Máquina: Coloco {z}')
    sleep(1)
    if x.upper() == 'PAR' and (z + y) % 2 == 1:
        print('Máquina: Ganhei, kkkkkk')
        break
  
    elif x.upper() == 'IMPAR' and (z + y) % 2 == 0:
        print(f'Máquina: Ganhei, kkkkkk')
        break
    else:
        s += 1
        print(f'Máquina: Parabéns, tu ganhou! Essa é tua {s}° vitória consecutiva!')
        print('-' * 64)