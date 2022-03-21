dados = list()
gurizada = list()
menorespesos = list()
pessoas = list()
cont = int(0)
aux = ''
maiorpeso = menorpeso = float(0)
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    gurizada.append(dados[:])
    dados.clear()
    cont += 1
    resposta = str(input('Quer continuar [s/n]? ')).upper().strip()[0]
    if resposta == 'N':
        break

for p in gurizada:
    if maiorpeso < p[1] or maiorpeso == 1:
        maiorpeso = p[1]
    if menorpeso > p[1] or menorpeso == 0:
        menorpeso = p[1]
    pessoas.append(p[0])
    

for p in gurizada:
    if p[1] == maiorpeso:
        dados.append(p[0])
    if p[1] == menorpeso:
        menorespesos.append(p[0])
    
                 
print(f'O maior peso foi o de {dados}: {maiorpeso}kg')
print(f' O menor peso foi o de {menorespesos}: {menorpeso}kg')
print(gurizada)
print(f' {"Foram" if len(pessoas) > 1 else "Foi"} {"cadastradas" if len(pessoas) > 1 else "cadastrada"} {len(pessoas)} pessoa{"s" if len(pessoas) > 1 else ""}')