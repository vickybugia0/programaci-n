import math

def obtener_cateto(nombre_cateto):
    while True:
        try:
            cateto = float(input(f"Ingrese el valor del {nombre_cateto} (mayor a 0): "))
            if cateto > 0:
                return cateto
            else:
                print("El valor debe ser mayor a 0. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

cateto1 = obtener_cateto("cateto 1")
cateto2 = obtener_cateto("cateto 2")

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"\nLa hipotenusa es: {hipotenusa:.2f}")
