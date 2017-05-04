try:
    documento1 = open("documento.txt", "r")
    documento2 = open("documento2.txt", "r")

    for i,linea in enumerate(documento1):
        print(linea,end='')
        # print(documento2.readline(),end='')
        if (linea != documento2.readline()):
            print("\n\nson distintos")



except (IOError, NameError) as er:
    print(er)
finally:
    documento1.close()
    documento2.close()
