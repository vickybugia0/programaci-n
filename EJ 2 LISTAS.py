import random


personajeA = [10, 50]  
personajeB = [8, 60]   

def combate_simple(personajeA, personajeB):
    turno = random.choice(["A", "B"])  
    print(f"Empieza el combate, turno de {turno}.\n")

    while personajeA[1] > 0 and personajeB[1] > 0:
        if turno == "A":
            personajeB[1] -= personajeA[0]  
            print(f"Personaje A ataca a B. Defensa de B: {personajeB[1]}")
            turno = "B"
        else:
            personajeA[1] -= personajeB[0] 
            print(f"Personaje B ataca a A. Defensa de A: {personajeA[1]}")
            turno = "A"

    if personajeA[1] <= 0:
        print("\n¡Personaje B ha ganado!")
    else:
        print("\n¡Personaje A ha ganado!")

def calcular_voltaje():
    intensidad = float(input("\nIntroduce la intensidad (amperios): "))
    resistencia = float(input("Introduce la resistencia (ohmios): "))
    voltaje = intensidad * resistencia
    print(f"El voltaje es: {voltaje} voltios")

combate_simple(personajeA, personajeB)

calcular_voltaje()
