#notiica al usuario de la velocidad que este lleva 
#si supera los 120Km/h se le notifica que va a exceso de velocidad

velocidad_max = int(input("Ingresa la velocidad en la que ibas en km/h:"))
limite = 120

if velocidad_max > limite:

    exceso = velocidad_max - limite

    print(f"Exceso de velocidad. Te pasaste por {exceso} km/h.")

elif velocidad_max == limite:

    print("Estás justo en el límite de velocidad.")

else:
    
    print("Velocidad permitida.")

