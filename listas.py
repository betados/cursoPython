lista = list("python is awesome")

print("lista[4]: ", lista[4])
print("lista[-2]: ", lista[-2])

""""[: 6], [7: 9], [10:], [2::5], [-3::-6] """
print("lista[: 6]: ", lista[: 6])
print("lista[7: 9]: ", lista[7: 9])
print("lista[10:]: ", lista[10:])
print("lista[2::5]: ", lista[2::5])
print("lista [-3::-6]: ", lista[-3::-6])


import random

aleatorios = []

for i in range(30):
    aleatorios.append(random.randrange(255))

print(aleatorios)

def mes(indice):
    indice = indice - 1
    if indice <1 or indice>11:
        print("eres tonto")
        return "tonto"
    else:
        lista =  ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return lista[indice]

print(mes(15))