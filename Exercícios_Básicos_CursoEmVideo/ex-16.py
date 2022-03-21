dicionario = dict()
gol = list()
lista = list()

while True:
    dicionario['nome'] = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    numpartidas = int(input('Quantas partidas {dicionario["nome"] jogou? '))
    for i in range(numpartidas):
        gol.append(int(input('Quantos gols {dicionario["nome"]} fez na partida {i + 1}: ')))
    
    dicionario['gols'] = gol[:]
    dicionario['total'] = sum(gol)
    dicionario['media'] = round(float(sum(gol)/numpartidas), 2)
    lista = dicionario.copy()
    gol.clear()
    
    while True:
        opt = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if opt in ('S', 'N'):
            break
        else:
            print('Digite uma opção válida [S/N]')
    if opt == 'N':
        break

print('-' * 48)