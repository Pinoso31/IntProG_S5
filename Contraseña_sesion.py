#Verificación de inicio de sesión
#Ingresar nombre de usuario y clave.
# Si el usuario es “admin” y la clave “1234admin”, permitir acceso.
# Si no, denegar.

usuario_real = "admin"
clave_real = "1234admin"
while True:

    print("*"*60)
    print("Hola, bienvenido al sistema de inicio de sesión")
    print("Por favor, ingrese sus credenciales")

    usuario = input("Ingrese su nombre de usuario: ")
    clave_usuario = input("Ingrese su clave: ")

    if usuario != usuario_real or clave_usuario != clave_real:
        print("Contraseña incorrecta. Intenta de nuevo.")
    else:
        print("*"*60)
        print("Los datos que has ingresado son correctos, bienvenido al sistema")
        print("*"*60)
   
 