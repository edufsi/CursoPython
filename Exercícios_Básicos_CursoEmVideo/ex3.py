numero = int(1)
precobarato = float(0)
produtomil = int(0)
total = float(0)
titulo = '\033[31mCADASTRO DE PRODUTOS'
centralizado = titulo.center(48,'*')
print('\033[31m-' * 48)
print(centralizado)
print('-' * 48, '\033[m')
while True:
    produto = input(f'Nome do {numero}° produto: ')
    preco = float(input(f'Preço do {numero} produto: R$'))
    if precobarato > preco or precobarato == 0:
        precobarato = preco
        produtobarato = produto
        total = total + preco
    if preco < 1000:
        produtomil += 1
    resposta = str('')
    print('-' * 48) 
    while resposta not in ['S', 'N']:
        resposta = str(input('Quer continuar (s/n)? ')).upper().split()[0]
    if resposta == 'N':
        break
    else:
        numero += 1
        print('-' * 30)
print(f'O total gasto na compra foi R${total:.2f}\nHá {produtomil} produtos custando menos de R$ 1000.00\nO produto mais barato foi {produtobarato}')