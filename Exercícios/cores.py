# O usuário deve inserir seu nome e sua cor primária favorita e então o nome do usuário deve aparecer daquela cor.

nome = str(input('Qual o teu nome? '))
cor = str(input('Qual a tua cor primária favorita? '))

# paleta = {'limpa':'\033[m', 
#         'azul':'\033[34m',
#          'vermelho':'\033[31m',
#          'amarelo':'\033[33m'}

if cor != 'Azul' and cor != 'Vermelho' and cor != 'Amarelo':
    print('Desculpa, não entendi a qual cor tu se referiu...')
else:
    if cor == 'Azul':
        print(f'\033[34mOlá, {nome}')    
    else:
        if cor == 'Vermelho':
            print(f'\033[31mOlá, {nome}')
        else:
            print(f'\033[33mOlá, {nome}')