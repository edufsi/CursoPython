import os
from time import sleep

def jogar(palavra):
    v = ' '
    cont = int(0)
    while True:
        tentativas1.append(list(str(input(f'Tentativa {cont + 1}: ')).strip().lower()))
        
        cont += 1
        lis = tentativas1[-1]
        
        
        i = int(0)
        for let in lis:
            
            if let in palavra and let == palavra[i]:
                print('\033[36m', let, '\033[m', end= "\n" if i + 1 == len(lis) else "  ")                
            elif let in palavra and let != palavra[i]:
                print('\033[33m', let, '\033[m', end= "\n" if i + 1 == len(lis) else "  ")
            else:
                print(let, end= "\n" if i + 1 == len(lis) else "  ")
            i += 1
            
        if tentativas1[-1] == palavra:
            break
        if cont == 6:
            break
        
            
        print('-' * 20)
    return(cont + 1)

    

os.system('clear') or None
tentativas1 = list()


p = str(input('Escreva uma palavra para o jogador 2: ')).strip().lower()
palavra1 = list(p)
os.system('clear') or None

p = str(input('Escreva uma palavra para o jogador 1: ')).strip().lower()
palavra2 = list(p)
os.system('clear') or None
print('VEZ DO JOGADOR 1'.center(20))
print('-' * 20)
x = jogar(palavra1)
sleep(1)
os.system('clear') or None
print('VEZ DO JOGADOR 2'.center(20))
print('-' * 20)
y = jogar(palavra2)
sleep(1)
os.system('clear') or None
if x < 7:
    print(f'O jogador 1 acertou com {x - 1} tentativa{"s" if x - 1 > 1 else ""}!')
else:
    print(f'O jogador 1 não acertou a palavra: ', end= '')
    for p in palavra1: 
        print(p.upper(), end= '')
if y < 7:
    print(f'\nO jogador 2 acertou com {y - 1} tentativa{"s" if x - 1 > 1 else ""}!')
else:
    print(f'\nO jogador 2 não acertou a palavra: ', end= '')
    for p in palavra2:
        print(p.upper(), end= '')
if x < y:
    print(f'\033[31m\nO JOGADOR 1 VENCEU!\033[m')
elif x > y:
    print(f'\033[31m\nO JOGADOR 2 VENCEU!\033[m')
elif x == y and x < 7:
    print('\033[31m\nEMPATOU!\033[m')
else:
    print('\033[31m\nNINGUÉM ACERTOU!\033[m')