# Soma de numeros solicitado ao usario, somando somente os pares
soma = 0
cont = 0 
for c in range(1,7):
    num = int(input('Digite {}° valor: '.format(c)))
    if num % 2 == 0:    
        soma += num
        cont += 1 
print('Você informou {} Pares, e a soma deles é {}'.format(cont, soma))
