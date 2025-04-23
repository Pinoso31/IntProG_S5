#notiica al usuario de la velocidad que este lleva 
#si supera los 120Km/h se le notifica que va a exceso de velocidad

velocidad_max = int(input("Ingresa la velocidad en la que ibas en km/h:"))

if velocidad_max > 120:
    print("Exceso de velocidad")
else:
    print("Velocidad permitida")
