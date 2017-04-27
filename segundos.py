while (True):
    resultado = 1
    totalSegundos = int(input("dame un número de segundos: "))

    segundos = totalSegundos % 60
    totalMinutos = (totalSegundos - segundos) / 60
    minutos = totalMinutos % 60
    totalHoras = (totalMinutos-minutos) /60
    horas = totalHoras % 24
    totalDias = (totalHoras-horas) / 24
    dias = totalDias % 365
    totalAnos = (totalDias - dias) / 365


    print("dias: %d \nhoras: %d \nminutos: %d \nsegundos: %d" % (dias, horas, minutos, segundos))