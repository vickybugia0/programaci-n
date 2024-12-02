def calcular_tarifa(tarifa_anual, edad, trabaja):
    if edad >= 18 and trabaja:
        # Mayor de edad y trabaja
        return tarifa_anual * 1.00
    elif edad < 18 and trabaja:
        # Menor de edad y trabaja
        return tarifa_anual * 0.95
    elif edad >= 18 and not trabaja:
        # Mayor de edad y no trabaja
        return tarifa_anual * 0.75
    elif edad < 18 and not trabaja:
        # Menor de edad y no trabaja
        return tarifa_anual * 0.50

# Ejemplo de uso
try:
    tarifa_anual = float(input("Introduce la tarifa anual del polideportivo: "))
    edad = int(input("Introduce tu edad: "))
    trabaja = input("¿Estás trabajando? (sí/no): ").strip().lower() == "sí"
    
    tarifa_calculada = calcular_tarifa(tarifa_anual, edad, trabaja)
    print(f"El precio de la tarifa es: {tarifa_calculada:.2f}")
except ValueError:
    print("Error: Introduce valores numéricos válidos.")