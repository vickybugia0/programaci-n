edad = int(input("Decime tu edad y te digo si podes pasar: "))
acompañado = str(input("indica si esta acompañado con si o no: "))
if edad >= 18:
    print("podes pasar")
else:
    if acompañado == "si":
        print("podes pasar")
    else:
        print("No podes pasar")