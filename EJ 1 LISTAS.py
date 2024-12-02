import random


ataqueA = 10
defensaA = 50

ataqueB = 8
defensaB = 60

def iniciar_combate(ataqueA, defensaA, ataqueB, defensaB):
    turno = random.choice(["A", "B"])
    print(f"El combate comienza y el primer turno es para el personaje {turno}.")

    while defensaA > 0 and defensaB > 0:
        if turno == "A":
 
            defensaB -= ataqueA
            print(f"Personaje A ataca a B. Defensa de B: {defensaB}")
            turno = "B" 
        else:
            defensaA -= ataqueB
            print(f"Personaje B ataca a A. Defensa de A: {defensaA}")
            turno = "A"  

    if defensaA <= 0:
        print("¡Personaje B ha ganado el combate!")
    else:
        print("¡Personaje A ha ganado el combate!")

iniciar_combate(ataqueA, defensaA, ataqueB, defensaB)
