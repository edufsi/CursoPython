from time import sleep as pausa
from random import randrange as rd
jogo = list()
jogos = list()
titulo = 'JOGO NA MEGA SENA'
print('-' * 38)
print(titulo.center(38))
print('-' * 38)

num = int(input('Quantos jogos tu quer sortear? '))
print('\n', '-' * 9, f'SORTEANDO {num} JOGOS', '-' * 10)
for l in range(num):
    for c in range(6):
        jogo.append(int(rd(61)))
        while jogo.count(jogo[-1]) > 1:
            jogo.pop()
            jogo.append(int(rd(61)))
    jogos.append(sorted(jogo[:]))
    jogo.clear()

for i in range(num):
    print(f'Jogo {i+1}: {jogos[i]}')
    pausa(0.6)