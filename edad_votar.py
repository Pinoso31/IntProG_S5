#Validar edad mínima para votar
#Ingresar la edad de una persona.
# Si la edad es mayor o igual a 18, mostrar "Puede votar".

print("--------------------------------------------------")
print("Bienvenido a tu mejor centro de votaciión")
votacion = int(input("Hola, buenos dias, ¿cuántos años tienes? "))

if votacion >= 18:
    print("Muy bien, ya tenes cédula de identidad, puedes votar")
else:
    print("No puedes votar, no tienes cédula de identidad")
print("--------------------------------------------------")