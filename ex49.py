
n1 = float(input('Digite um numero para ver sua tabuada:'))
for c in range(1, 11):
    print('{:.0f} x {} = {:.0f}'.format(n1, c, n1*c))