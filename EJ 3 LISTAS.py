asignaturas = input("Insertar la lista de las asignaturas: ").split(',')

asignaturas = [asignatura.strip() for asignatura in asignaturas]

for asignatura in asignaturas:
    num_alumnos = int(input(f"Número de alumnos en {asignatura}: "))

    puntuaciones = []
    for i in range(num_alumnos):
        puntuaciones.append(float(input(f"Puntuación del alumno {i+1} en {asignatura}: ")))

    media = sum(puntuaciones) / num_alumnos
    suspensos = sum(1 for puntuacion in puntuaciones if puntuacion < 5)

    print(f"[{asignatura}, {num_alumnos} alumnos. Nota media: {media:.1f}, Suspensos: {suspensos}]")
