import math


def calculadora():
    while True:
    
        comando = input("Ingrese los valores de A y B separados por un espacio o 'SAL' para salir: ")

        if comando.upper() == 'SAL':
            print("Apagando la calculadora.")
            break

        try:
            A, B = map(float, comando.split())

            operacion = input("Ingrese el número de la operación (1: raíz cuadrada de la suma, 2: A/B, 3: (A*B)/2.5): ")

            if operacion == '1':
                resultado = math.sqrt(A + B)
                print(f"Raíz cuadrada de la suma de {A} y {B} es: {resultado}")

            elif operacion == '2':
                if B != 0:
                    resultado = A / B
                    print(f"{A} dividido por {B} es: {resultado}")
                else:
                    print("Error: División por cero no permitida.")

            elif operacion == '3':
                resultado = (A * B) / 2.5
                print(f"El resultado de ({A} * {B}) / 2.5 es: {resultado}")

            else:
                print("Operación no válida. Intente nuevamente.")

        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar dos números separados por un espacio.")
