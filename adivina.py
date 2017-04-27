import random
noAcertado = True
numero = random.randrange(100)
while (noAcertado):
    entrada = int(input("adivina: "))
    if entrada > numero:
        print("el que buscas es menor")
    if entrada < numero:
        print("el que buscas es mayor")
    if entrada == numero:
        noAcertado = False
print("¡¡Acertado!!")
