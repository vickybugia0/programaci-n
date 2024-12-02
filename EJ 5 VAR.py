def elegir_ingrediente(vegetariana):
    if vegetariana:
        print("Ingredientes vegetarianos disponibles: Pimiento, Tofu")
        ingrediente = input("Elige un ingrediente (Pimiento/Tofu): ").strip().lower()
        if ingrediente == "pimiento" or ingrediente == "tofu":
            return ingrediente
        else:
            print("Ingrediente no válido, seleccionando Pimiento por defecto.")
            return "pimiento"
    else:
        print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón, Salmón")
        ingrediente = input("Elige un ingrediente (Peperoni/Jamón/Salmón): ").strip().lower()
        if ingrediente in ["peperoni", "jamón", "salmon", "salmón"]:
            return ingrediente
        else:
            print("Ingrediente no válido, seleccionando Peperoni por defecto.")
            return "peperoni"

def preparar_pizza():
    tipo = input("¿Quieres una pizza vegetariana? (sí/no): ").strip().lower()
    vegetariana = tipo == "sí"
  
    ingredientes = ["mozzarella", "tomate"]
    
    ingrediente_adicional = elegir_ingrediente(vegetariana)
    ingredientes.append(ingrediente_adicional)
    
    tipo_pizza = "vegetariana" if vegetariana else "no vegetariana"
    print(f"\nHas elegido una pizza {tipo_pizza} con los siguientes ingredientes: {', '.join(ingredientes)}.")

preparar_pizza()
StopIteration