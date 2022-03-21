dicionario = dict()
lista = list()
soma = int()
gol = list()
while True:
    dicionario['nome'] = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    numpartidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou: '))
    for i in range(numpartidas):
        gol.append(int(input(f'Quantos gols {dicionario["nome"]} fez na {i + 1} partida: ')))
    dicionario['gols'] = gol[:]
    media = round(float(sum(gol) / numpartidas), 2)
    dicionario['media'] = media
    dicionario['total'] = sum(gol)
    lista.append(dicionario.copy())
    gol.clear()
    print('-' * 60)
    while True:
        opt = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if opt in ('S', 'N'):
            break
        else:
            print('Digite uma opção válida [S/N]:')
    print('-' * 60)
    if opt == 'N':
        break
print('COD'.center(5), 'NOME'.center(15), 'GOLS'.center(24), 'MEDIA DE GOLS')
print('-' * 60)
for n, d in enumerate(lista):
    print(n + 1, '-' * 3, d['nome'].center(15), d['gols'], ' ' * (27 - 3 * len(d['gols'])), d['media'])
opt = int(input('Digite o código de um dos jogadores para saber os detalhes'))
while opt != 999:

    for d in lista:
        if d == lista[opt - 1]:
            print(f'{d["nome"]} fez um total de {d["total"]} gol{"s " if d["total"] > 1 else " "}jogando {len(d["gols"])} partida{"s " if len(d["gols"]) > 1 else " "}')
            for n, v in enumerate(d['gols']):
                print(f'No jogo {n + 1}, {d["nome"]} fez {d["gols"][n]} gol{"s" if d["gols"][n] > 1 else " "}')
    print('-' * 60)
    opt = int(input('Digite o código de um dos jogadores para saber os detalhes'))