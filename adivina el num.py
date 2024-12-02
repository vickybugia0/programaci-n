import random
 
def guess(x) :
        random_number = random.randint(1, x)
        guess = 0 
        while guess != random_number:
            guess = int(input(f'Dime un número de 1 al {x} : '))
            if guess < random_number:
                print('Trata de nuevo, muy bajo')
            if guess > random_number :
                print('Trata de nuevo, muy alto')
            elif guess == random_number:
                print(f'Felicitaciones! Adivinaste el número! {guess} ')
                break

guess(20)