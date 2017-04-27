while True:
    try:
        n = int(input("dámelo: "))
        break
    except ValueError:
        print("no es un numero")
print("es un numero")
