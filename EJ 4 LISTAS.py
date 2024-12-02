nombres = []

while True:
    nombre = input("Introduce un nombre (-1 para terminar): ").strip()
    
    if nombre == "-1":
        break
    
    nombres.append(nombre)

if nombres:
    nombre_mas_comun = max(nombres, key=nombres.count)
    cantidad = nombres.count(nombre_mas_comun)

    for nombre in set(nombres):  
        print(f"{nombre}: {nombres.count(nombre)}")

    print(f"El nombre más común es {nombre_mas_comun} con {cantidad} repeticiones.")

