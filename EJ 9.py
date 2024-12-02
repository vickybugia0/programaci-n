password_guardada = "VICKY1234"

def verificar_contraseña(contraseña):
    if contraseña == password_guardada:
        print("Bienvenida Vicky")
    else:
        print("Ordenador bloqueado. Contraseña incorrecta.")

# Pedir contraseña 
intento_contraseña = input("Introduce la contraseña: ")
verificar_contraseña(intento_contraseña)
