
import random


emails = []
while True:
    email = input("Introduce un email (o 'FIN' para terminar): ")
    if email.upper() == 'FIN':
        break
    emails.append(email)

num_ayudas = int(input("¿Cuántas ayudas deseas repartir? "))

beneficiarios = random.sample(emails, num_ayudas)

print("Beneficiarios seleccionados:", beneficiarios)