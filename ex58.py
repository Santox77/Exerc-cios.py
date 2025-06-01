import random
computador = random.randint(1, 10)
numero = int(input("Digite um numero de 1 a 10:"))
contador = 1
while numero != computador:
    contador += 1 
    if numero < computador:
        numero = int(input("Mais... Tente mais uma vez:"))
    else: 
        numero = int(input('Menos... Tente mais uma vez:')) 
print("Acertou com {} tentativas. Parabens !".format(contador))   
        