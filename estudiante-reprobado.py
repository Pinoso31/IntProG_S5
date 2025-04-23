#Evaluar si un estudiante aprueba o reprueba
# Ingresar una calificación.
# Si es mayor o igual a 70, mostrar "Aprobado"; de lo contrario, "Reprobado".

calificacion = float(input("Ingrese la calificación del estudiante: "))

if 0 <= calificacion <= 100:
    if calificacion >= 70:
        print("OSHEE, estás aprobado...otro level.")
    else:
        print("JAJAJA, estás reprobado mongolo.")