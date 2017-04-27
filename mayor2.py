# Calcular el mayor de dos números

a = int(input("Dame un número: "))
b = int(input("Dame otro número: "))

if a > b:
    print("%d es mayor que %d" % (a, b))
elif b > a:
    print("%d es mayor que %d" % (b, a))
else:
    print("ambos son iguales")
