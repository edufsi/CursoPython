aprovados = list()
reprovados = list()
lista = list()
notas = list()
alunos = list()
ponder = int(0)

numaval = int(input('Registrar quantas notas? '))

while True:
    somanotas = float(0)
    alunos.append(str(input('Nome da(o) aluna(o): ')).capitalize())
    for i in range(numaval):
        notas.append(float(input(f'Nota {i + 1}: : ')))
   
    alunos.append(notas[:])
    for i in range(numaval):
        somanotas += notas[i]
    alunos.append(round(somanotas/numaval,2))
    lista.append(alunos[:])
    notas.clear()
    alunos.clear()
    while True:
        opt = str(input('Quer continuar [s/n]? ')).upper().strip()[0]
        if opt in ('S', 'N'):
            break
    if opt == 'N':
        break
print('-' * 38)
lista = sorted(lista)
for i in range(len(lista)):
    if lista[i][2] >= 6:
        print(i + 1, ' ' * 4, lista[i][0].ljust(25), '\033[32m', round(lista[i][2],2), '\033[m')
        aprovados.append(lista[i][0])
    else:
        print(i + 1, ' ' * 4, lista[i][0].ljust(25), '\033[31m', round(lista[i][2],2), '\033[m')
        reprovados.append(lista[i][0])
print('-' * 38)
print('\033[32mAPROVADOS:\033[m ', aprovados)
print('\033[31mREPROVADOS:\033[m ', reprovados)
ponder = int(input('Digite o número de um aluno para saber suas notas [999 para sair]: '))
while ponder != 999:
    while True:
        if ponder > len(lista) or ponder < 1:
            print('Isso não é um código válido')
            ponder = str(input('Digite o número de um aluno para saber suas notas [999 para sair]: '))
        else: 
            break
    print(f'Notas de {lista[ponder - 1][0]}: {lista[ponder - 1][1]}')
    print('-' * 38)
    ponder = int(input('Digite o número de um aluno para saber suas notas [999 para sair]: '))