def invertir(cadena):
    cadenaInvertida=""
    for i in range(len(cadena)):
        # print(cadena[len(cadena) - 1 - i])
        cadenaInvertida += cadena[len(cadena)-1-i]
    return cadenaInvertida

def esPalindroma(cadena):
    if cadena == invertir(cadena):
        return True
    else:
        return False

print(invertir("alvaro"))
print(esPalindroma("ada"))
