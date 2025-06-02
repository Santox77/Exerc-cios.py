print('=-=' * 10)
n = int(input("Digite um numero:"))
r = int(input("Digite uma PA:"))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} → ", end="")
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input("Quantos termos voce quer ver mais ? "))
print(f"Progressão total foi de {total}")
    