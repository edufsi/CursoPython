linha = list()
coluna = list()
copia = list()
somapar = somaimpar = soma_3_coluna = num = int(0)

for i in range(3):
    for j in range (3):
        coluna.append(int(input('Digite um número: ')))
    linha.append(c[:])
    coluna.clear()


   
for coluna in linha:
    for v in c:
  
            
        if v % 2 == 0:
            somapar += v
        elif v % 2 == 1:
            somaimpar += v
    
for i in range(0,3):
    soma_3_coluna += l[2]

    
    
    
    
for i in range(0,3):
    for j in range(0,3):
        print(l[i][j], end='  ')
    print()
print(somapar)
print(somaimpar)
print(soma_3_coluna)
print(max(l[1]))
