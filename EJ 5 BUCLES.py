# Definir el PIN 
PIN_SECRETO = "123409"

intentos_permitidos = 3

intentos = 0

while intentos < intentos_permitidos:
    pin_ingresado = input("Ingresa el PIN: ")
    
    if pin_ingresado == PIN_SECRETO:
        print("Login correcto")
        break
    else:
        intentos += 1
        print(f"PIN incorrecto. Intentos restantes: {intentos_permitidos - intentos}")

if intentos == intentos_permitidos:
    print("Llamando al policía...")
