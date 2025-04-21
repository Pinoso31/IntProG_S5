rango_inicial = int(input("Ingrese el rango inicial: "))
rango_final = int(input("Ingrese el rango final: "))

if(rango_inicial < rango_final):
  
     numero = int(input("Dime un numero: "))
     if(numero >= rango_inicial and numero <= rango_final):
        print("el numero esta dentro del rango")
     else:
      print("El numero esta fuera del rango")
else:
    print("El rango inicial debe ser menor que el rango final")