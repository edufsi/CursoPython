from math import floor
valor = float(input('Digita o valor a ser sacado: R$ '))
notascinquenta = int(floor(valor/50))
if notascinquenta != 0:
    print(f'Total de {notascinquenta} cédulas de R$50.00')
valor -= notascinquenta * 50
notasvinte = int(floor(valor/20))
if notasvinte != 0:
    print(f'Total de {notasvinte} cédulas de R$20.00')
valor -= notasvinte * 20
notasdez = int(floor(valor/10))
if notasdez != 0:
    print(f'Total de {notasdez} cédulas de R$10.00')
valor -= notasdez * 10
notascinco = int(floor(valor/5))
if notascinco != 0:
    print(f'Total de {notascinco} cédulas de R$5.00')
valor -= notascinco * 5
moedasum = int(floor(valor))
if moedasum != 0:
    print(f'Total de {moedasum} cédulas de R$1.00')
valor = (valor - moedasum) *10
moedascinquenta = int(valor//5)
if moedascinquenta != 0:
    print(f'Total de {moedascinquenta} moedas de R$00.50')
valor -= moedascinquenta * 5
moedasvinte = int(valor//2)
if moedasvinte != 0:
    print(f'Total de {moedasvinte} moedas de R$00.20')
valor -= moedasvinte * 2
moedasdez = int(valor)
if moedasdez != 0:
    print(f'Total de {moedasdez} moedas de R$00.10')
valor -= moedasdez 
moedascinco = int(floor(valor/5))