import random

def computer_guess(x):
     low = 1
     high = x
     feedback = " "
     while feedback!= 'c':
          guess = random.randint (low, high)
          feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
          
          if feedback == "l" :
               low = guess + 1
               guess = low 
               
          elif feedback == 'h':
               high= guess - 1
               guess =  high
               
          elif feedback == 'c':
               print(f'Felicitaciones! Adivinaste el número! {guess} correctamente')


computer_guess(20)

