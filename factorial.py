
while (True):
    resultado = 1
    numero = int(input("dame un número para calcular su factorial: "))
    for i in range(1,numero+1):
        resultado = resultado *i

    print(resultado)