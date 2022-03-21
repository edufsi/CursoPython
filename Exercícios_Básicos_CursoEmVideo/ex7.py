lista = []
posicao = 0
aux = int(0)
for i in range (5):
    
    lista.append(int(input('Digite um número inteiro: ')))
    aaaaa = lista[i]
    for c in range(len(lista)):
        
        if lista[i] < lista[c]:
            
            aux = lista[i]
            lista[i] = lista[c]
            lista[c] = aux
    aaaaa= lista.index(aaaaa)
    
    print(f'Valor colocado na {aaaaa + 1}° posição')
    print('-' * 38)
print('\033[32m', lista)