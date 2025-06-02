n = int(input("Digite um numero:"))
r = int(input("Digite uma PA:"))
pam = n + ( r * 9 )
c = n
while c <= pam:
    print(f"{c}", end="")
    print(' → ' if c < pam else ' = ', end='')
    c += r
print("FIM")