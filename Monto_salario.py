#Cálculo de propina según satisfacción
# Ingresar monto total y nivel de satisfacción (buena/mala).
# Si es buena, calcular 15% propina; si es mala, 5%.
# Mostrar total a pagar.

salario = float(input("Ingresa el monto total de tu salario: "))
satisfacion = input("¿Que tan bueno fue tu servicio (buena/mala) : ")

if satisfacion  == "buena":
    
    propina = salario * 0.15

elif satisfacion  == "mala":
    
    propina = salario * 0.5

print("El monto total a pagar es: ", salario + propina)
