#Verificar si un número es par y es positivo
# Ingresar un número.
# Si es mayor que 0, mostrar "El número es positivo".
# Si es divisible por 2, mostrar “El número es par” 
 
numero = int(input("Ingrese un numero: "))

if (numero > 0 and numero%2==0):
    print("El numero es positivo y par")
else:
    print("No cumple con las condiciones")

