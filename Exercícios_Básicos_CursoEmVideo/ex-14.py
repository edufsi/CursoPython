import datetime
data = datetime.date.today()
ano = int(data.strftime("%Y"))
dicionario = dict()
dicionario['nome'] = str(input('Digite seu nome: '))
dicionario['idade'] = ano - int(input('Digite seu ano de nascimento: '))
dicionario['ctps'] = int(input('Carteira de Trabalho [0 se não possuir]: '))
if dicionario['ctps'] == 0:
    print(f'Nome: {dicionario["nome"]}\nIdade: {dicionario["idade"]}')
else: 
    dicionario['contratacao'] = int(input('Digite o ano de contratação: '))
    dicionario['contribuicao'] = ano - dicionario['contratacao']
    dicionario['salario'] = float(input ('Digite o salário: R$'))
    print(f'Nome: {dicionario["nome"]}\nIdade: {dicionario["idade"]}\nCTPS: {dicionario["ctps"]}\nAno de contratação: {dicionario["contratacao"]}\nAnos de contribuição: {dicionario["contribuicao"]}\nSalário: R${dicionario["salario"]}')