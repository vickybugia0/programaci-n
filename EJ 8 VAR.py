import math

def calcular_hipotenusa(cateto1, cateto2):
    if cateto1 <= 0 or cateto2 <= 0:
        print("Error: Los catetos deben ser mayores que cero.")
        return
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print(f"La hipotenusa es: {hipotenusa}")


try:
    cateto1 = float(input("Introduce el valor del primer cateto: "))
    cateto2 = float(input("Introduce el valor del segundo cateto: "))
    calcular_hipotenusa(cateto1, cateto2)
except ValueError:
    print("Error: Introduce valores numéricos válidos.")