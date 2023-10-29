X = float(input('Digite o conprimento do primeiro lado: '))
Y = float(input('Digite o comprimento do segundo lado: '))
Z = float(input('Digite o comprimento do terceiro lado: '))
if X <= 0 or Y <= 0 or Z <= 0:
    print('\033[31mTRATA-SE DE UM BURACO!')
else:
    if X > Y and X > Z:
        maiorlado = X
        aux = float(X)
    elif Y > X and Y > Z:
        maiorlado = Y
        aux = float(Y)
    elif Z > X and Z > Y:
        maiorlado = Z
        aux = float(Z)
    else:
        maiorlado = X
        aux = X
    if maiorlado > X + Y + Z - aux:
        print(f'\033[31mNão é possível fazer um triângulo com lados {X},{Y} e {Z}\033[m')
    elif maiorlado <= X + Y + Z - aux and X == Y and X == Z:
        print(f'\033[32mÉ possível fazer um triângulo EQUILÁTERO com lados {X},{Y} e {Z}\033[m')
    elif maiorlado <= X + Y + Z - aux and X == Y or X == Z or Z == Y:
        if maiorlado*2 == X**2 + Y**2 + Z**2 - aux**2:
            print(f'\033[32mÉ possível fazer um triângulo RETÂNGULO e ISÓSCELES com lados {X},{Y} e {Z}\033[m')
        else:
            print(f'\033[32mÉ possível fazer um triângulo ISÓSCELES com lados {X},{Y} e {Z}\033[m')
    elif maiorlado <= X + Y + Z - aux and X != Y and X != Z and Z != Y:
        if maiorlado*2 == X**2 + Y**2 + Z**2 - aux**2:
            print(f'\033[32mÉ possível fazer um triângulo RETÂNGULO e ESCALENO com lados {X},{Y} e {Z}\033[m')
        else:
            print(f'\033[32mÉ possível fazer um triângulo ESCALENO com lados {X},{Y} e {Z}\033[m')
    else:  
            print(f'\033[32mÉ possível fazer um triângulo com lados {X},{Y} e {Z}\033[m')
