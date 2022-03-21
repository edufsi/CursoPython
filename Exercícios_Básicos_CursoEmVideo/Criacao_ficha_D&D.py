from random import randrange as rd
from math import floor
rolagens = list()
ficha = list()
atributos= list()
minimo = mini = int()
fi = {'FOR' : ' ',
'DES' : ' ',
'CON' : ' ',
'SAB' : ' ',
'INT' : ' ',
'CAR' : ' '}


for a in range(6):
    soma = int(0)
    for dados in range(4):
        rolagens.append(rd(1,7))
    minimo = rolagens.index(min(rolagens))
    mini = min(rolagens)
    for i in range(minimo):
        print(rolagens[i], end= ', ')
    
    print(f'\033[31m{mini}\033[m{", " if minimo != 3 else ": "}', end='')
    for i in range(minimo + 1, 4):
        print(f'{rolagens[i]}{", " if i != 3 else ": "}', end='')
    
    x = sorted(rolagens)
    x.pop(0)
    for e in x:
        soma += e
    print(soma)
    print('-' * 54)
    atributos.append(soma)
    rolagens.clear()
    ficha.append(atributos[:] )
    atributos.clear()
ficha.sort()

for i in range(6):
    ficha[i].append(int(floor((ficha[i][0] - 10) / 2)))
print('VALORES DOS SEUS ATRIBUTOS:')
print(f'\033[32m{ficha}\033[m')
print('-' * 54)
for i,v in enumerate(ficha):
    
    while True:
        carac = str(input(f'Em qual atributo deverá ser colocado o valor {ficha[i][0]} ({"+" if ficha[i][1] > 0 else ""}{ficha[i][1]})? ')).upper().strip()
        
            
        if carac[:3] in ('FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR'):
            break
        else:

            print('Digite um atributo válido [for, des, con, int, sab, car]:')
    if fi[carac] != ' ':
        ficha.append(fi[carac][:])
        fi.pop(carac)
        fi[carac] = ficha[i].copy()
        
            
    else:
        fi[carac] = ficha[i].copy()
    for i, v in fi.items():
        print(f'{i}: {v}')
    print('-' * 54)