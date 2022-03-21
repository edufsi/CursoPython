dicionario = dict()
lista = list()
maiores_media = list()
soma = int()
t = ''
while True:
    dicionario['nome'] = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    dicionario['sexo'] = str(input('Digite o gênero da pessoa: ')).strip().capitalize()[0]
    dicionario['idade'] = int(input('Digite a idade da pessoa: '))
    lista.append(dicionario.copy())
    while True:
        opt = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if opt in ('S', 'N'):
            break
        else:
            print('Digite uma opção válida [S/N]')
    if opt == 'N':
        break
print('-' * 48)
print(f'Fo{"ram" if len(lista) > 1 else "i"} cadastrada{"s" if len(lista) > 1 else ""} {len(lista)} pessoa{"s" if len(lista) > 1 else ""}')
print('-' * 48)
for d in lista:
    soma += d['idade']
media = round(soma / len(lista), 2)
print(f'A média da{"s idades foi:" if len(lista) > 1 else " idade é a própria idade:"} {media}')
print('-' * 48)
for d in lista:
    if d['sexo'] == 'F' and t == '':
        print(f'As pessoas do gênero feminino cadastradas foram: ', end='')
        t = 'T'
    elif d == lista[-1] and d['sexo'] != 'F' and t != 'T':
        print('Não foram registradas pessoas do gênero feminino')
        print('-' * 48)
for d in lista:
    if d['sexo'] == 'F' and t == 'T':
        print(f'{d["nome"]}', end="." if d == lista[-1] else ", ")
    if d['idade'] > media:
        maiores_media.append(d.copy())
print('\n', '-' * 48)
print('Lista das pessoas que estão acima da média de idade:')
for d in maiores_media:
    print(d)