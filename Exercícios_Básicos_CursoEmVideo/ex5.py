valores = []
aux = int(0)
auxi = int(0)
for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))
    if valores[c] > aux or len(valores) == 1:
        aux = int(valores[c])
    if valores[c] < auxi or len(valores) == 1:
        auxi = int(valores[c]) 
va = valores[:]
ca = valores [:]
cont = 0
print(f'O menor valor foi {auxi}, localizado na posição', end=' ')
while auxi in va:
    print(va.index(auxi) + cont, end='..')
    va.remove(auxi)
    cont += 1
cont = 0
print(f'\nO maior valor foi {aux}, localizado na posição', end=' ')
while aux in ca:
    print(ca.index(aux) + cont, end='.. ')
    ca.remove(aux)
    cont += 1
print('\n', valores)