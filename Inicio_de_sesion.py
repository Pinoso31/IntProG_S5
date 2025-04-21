#Detectar si un usuario está inactivo por más de 30 días
 #Ingresar fecha de último inicio de sesión.
 #Calcular los días transcurridos.
# Si son más de 30, mostrar “Cuenta inactiva”

import datetime as dt

print("Bienvenido a Uam virtual")
inicio_sesion = input("Ingrese cuando fue tu ultimo inicio de sesion en formato YYYY-MM-DD: ")
inicio_sesion = dt.datetime.strptime(inicio_sesion, "%Y-%m-%d")

fecha_actual = dt.datetime.now()

contar_dias = (fecha_actual - inicio_sesion).days
if contar_dias > 30:
    print("estás perdido en el tiempo")
else:
    print("Tamos activo papi")

                
