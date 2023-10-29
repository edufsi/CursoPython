from random import randrange as rd
from time import sleep as pausa
lista = list()
dicionario = dict()
posicao = algo = int(0)
for i in range(4):
    jogador = str(input('Nome do jogador: '))
    dicionario[jogador] = rd(1,7)
    lista.append(dicionario[jogador])
    

lista.sort(reverse = True)
for h in range(4):
    for i,v in dicionario.items():
  
   
        if dicionario[i] == lista[h]:
            if lista[h] != algo:
            
                posicao += 1
            pausa(1)
            print(f'O {posicao}° lugar é: {i} com {v}')
            dicionario[i] = ''
            algo = lista[h]
            lista[h] = ' '