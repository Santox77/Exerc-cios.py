from datetime import date
atual = date.today().year
print("Este é o ano que estamos: {}".format(atual))
cont = 0
cont2 = 0 
for c in range(1, 8):
    nasci = int(input("Digite o nascimento da {}° pessoa:".format(c)))
    idade = atual - nasci 
    if idade > 2007:
        cont2 += 1
    else:
        cont += 1      
print(f'O total de pessoas que tem mais de 18 anos é: {cont}')
print(f'O total de pessoas que tem menos de 18 anos é: {cont2}')
