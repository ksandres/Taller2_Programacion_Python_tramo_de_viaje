tiempoTotalmin = 0

while (True):
    tiempo = int(input("ingrese el tiempo de vieje del tramo en minutos (0 para finalizar)"))

    if (tiempo == 0):
        break
    tiempoTotalmin += tiempo
horas = int(tiempoTotalmin / 60)
min = tiempoTotalmin % 60
print("Tiempo total de vieje: " + str(horas) + " horas " + str(min) + "minutos")
