numero = int(input("Introduce un número para calcular la tabla de multiplicar: "))

for i in range(1, 21): 
    print(f"{numero} x {i} = {numero * i}")



primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

primos.sort(reverse=True)

print(primos)
