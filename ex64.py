cont = 0
numero = 0
n = int(input('Digite um numero [999 para parar]:'))
while n != 999:
    cont += 1
    numero = n + numero
    n = int(input('Digite um numero [999 para parar]:'))
print("Você digitou {} e a soma dos numeros é {}".format(cont, numero))
    