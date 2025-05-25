import random

def jogo_de_advinhacao():
    numero = random.randint(1, 10)  
    while True:
        print("Adivinhe o número de 1 a 10:", end="")
        advinhe = int(input())

        if advinhe == numero:
            print("Parabéns! Você acertou.")
            break
        else:
            print("Tente novamente")

while True:
    jogo_de_advinhacao()
    
    jogar_novamente = input("Deseja jogar novamente? (Sim ou Não): ")
    if jogar_novamente.lower() != "sim":
         break 

print("Fim do jogo.")

import random

def jogo_de_advinhação():
    numero = random.randint(1, 10)
    while True:
        print("Adivinhe o número de 1 a 10:", end="")
        advinhe = int(input())

        if advinhe == numero:
            print("Parabéns! Você acertou.")
            break
        else:
            print("Tente novamente")
while True:
    jogo_de_advinhação()
    
    jogar_novamente = input("Deseja jogar novamente? (Sim ou Não): ")
    if jogar_novamente.lower() != "Sim":
        break

print("Fim do jogo.")
