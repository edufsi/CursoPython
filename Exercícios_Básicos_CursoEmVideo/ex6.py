valores = []
i = -1
pops = 0
while True:
    valores.append(int(input('Digite um número: ')))
    i += 1
    if valores[i - pops] in valores[:-1]:
        print('Valores duplicados não serão adicionados.')
        valores.pop()
        pops += 1
    print('-' * 38)
    resposta = input('Quer continuar? ').upper().strip()[0]
    if resposta == 'N':
        break
    print('-' * 38)
print(f'Tu digitou {valores}')