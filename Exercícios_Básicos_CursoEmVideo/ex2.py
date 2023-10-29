n = int(0)
while True:
    n = int(input('Digite um número positivo (negativo: sair): '))
    print('-' * 45)
    if n < 0:
        break
    print(f'TABUADA DO {n}'.center(45,'-'))
    for i in range (0,11):
        print(f'{n:2} x {i} = {n*i}')
    print('-' * 45)