nome = str(input('Qual o teu nome? '))
cor = str(input('Qual a tua cor favorita? '))
paleta = {'limpa':'\033[m', 
          'azul':'\033[34m',
          'vermelho':'\033[31m',
          'amarelo':'\033[33m',
          'branco':'\033[97m',
          'preto':'\033[30m',
          'verde':'\033[32m',
          'ciano':'\033[36m'}
if cor.lower() != 'azul' and cor.upper() != 'VERMELHO' and cor.upper() != 'AMARELO':
    print('Desculpa, não entendi a qual cor tu se referiu...')
else:
    if cor.upper() == 'AZUL':
        print('{}Olá, {}'.format(paleta['azul'], nome))    
    else:
        if cor.upper() == 'VERMELHO':
            print('{}Olá, {}'.format(paleta['vermelho'], nome))
        else:
            print('{}Olá, {}'.format(paleta['amarelo'], nome))