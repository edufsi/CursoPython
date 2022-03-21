l = list()
c = list()
copia = list()
somapar = somaimpar = somatercol = num = int(0)

for i in range(3):
    for j in range (3):
        c.append(int(input('Digite um número: ')))
    l.append(c[:])
    c.clear()


#Para cada coluna numa linha e pro valor em cada coluna, verificar se é par ou impar e se está na terceira coluna:    
for c in l:
    for v in c:
  
            
        if v % 2 == 0:
            somapar += v
        elif v % 2 == 1:
            somaimpar += v
    
for i in range(0,3):
    somatercol += l[2]

    
    
    
    
for i in range(0,3):
    for j in range(0,3):
        print(l[i][j], end='  ')
    print()
print(somapar)
print(somaimpar)
print(somatercol)
print(max(l[1]))