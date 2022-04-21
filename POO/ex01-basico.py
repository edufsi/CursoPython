'''
Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do lado, Mostrar valor do lado e Calcular área
'''

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudar_lado(self, valor):
        self.lado = valor
        
    def print_lado(self):
        print(f'O valor do lado do quadrado é {self.lado}')
        
    def calcular_area(self):
        self.area = self.lado ** 2
        print(f'A área do quadrado é {self.area}')
        


'''
Crie uma classe retângulo que modele um retângulo:

Atributos: LadoA, LadoB
Métodos: Mudar valor dos lados, Mostrar valor dos lados, Calcular área e Calcular perímetro

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois deve criar um objeto com as medidas e calcular a quantidade de pisos necessarios para o local
'''

class Retangulo:
    def __init__(self):
        self.altura = float(input('Qual a altura do retângulo? '))
        self.largura = float(input('Qual a largura do retângulo? '))
    
    def mudar_lados(self): 
        print(f'O atual valor da altura do retângulo é {self.altura} e o atual valor da largura do retângulo é {self.largura}.')
        while True:
            opt = str(input('Quer mudar algum dos lados [s/n]? ')).strip().lower()[0]
            if opt == 'n':
                break
            elif opt == 's':
                while True:
                    lado = str(input('Qual [largura/altura]? ')).strip().lower()
                    if lado == 'altura':
                        self.altura = float(input('Digite um novo valor para a altura: '))
                        print(f'Agora a altura do retângulo é {self.altura} e a largura é {self.largura}')
                        break
                    elif lado == 'largura':
                        self.largura = float(input('Digite um novo valor para a largura: '))
                        print(f'Agora a largura do retângulo é {self.largura} e a altura é {self.altura}')
                        break

    def imprimir_lados(self):
        print(f'ALTURA = {self.altura} e LARGURA = {self.largura}')
        
    def calcular_area(self):
        print(f'A área do retângulo é {self.altura * self.largura}')
        return self.altura * self.largura
    
    def calcular_perimetro(self):
        print(f'O perímetro do retângulo é {self.altura * 2 + self.largura * 2}')
        return self.altura * 2 + self.largura * 2
print('Dimensões do terreno:')
retangulo = Retangulo()
area_terreno = retangulo.calcular_area()
print('-' * 30)
print('Dimensões do piso:')
pisos = Retangulo()
area_pisos = pisos.calcular_area()
print('-' * 30)
print(f'Você precisará de um total de: {area_terreno * 1.1 / area_pisos} pisos, considerando possíveis perdas')

