lista = [[], []]
while True:
    x = int(input('Digite um número: '))    
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
    while True:
        opt = str(input('Quer continuar [s/n]? ')).upper().strip()[0]
        if opt in ('S', 'N'):
            break
    if opt == 'N':
        break

print(f'Valor{"es" if len(lista) > 1 else ""} par{"es" if len(lista) > 1 else ""}: {lista[0]}')
print(f'Valor{"es" if len(lista) > 1 else ""} ímpar{"es" if len(lista) > 1 else ""}: {lista[1]}')
print(lista)