class Calculadora:

    # def __init__(self):
    #     pass

    def sumar(self, *numeros):
        suma = 0
        for numero in numeros:
            suma += numero

        return suma

    def multiplicar(self, *numeros):
        producto = 1
        for numero in numeros:
            producto *= numero

        return producto

    def mediar(self, *numeros):
        media = 0
        for numero in numeros:
            media += numero

        return media/len(numeros)