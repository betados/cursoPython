a = int(input("Dame un número: "))
b = int(input("Dame otro número: "))
c = int(input("Dame otro número más: "))

lista = [a, b, c]

for numeroI in lista:
    for numeroJ in lista:
        if numeroI >= numeroJ:
            mayor = numeroI
        else:
            mayor = numeroJ

lista.remove(mayor)

for numeroI in lista:
    for numeroJ in lista:
        if numeroI >= numeroJ:
            mediano = numeroI
        else:
            mediano = numeroJ

lista.remove(mediano)

menor = lista[0]

print("mayor= %d" %(mayor))
print("mediano= %d" %(mediano))
print("menor= %d" %(menor))
