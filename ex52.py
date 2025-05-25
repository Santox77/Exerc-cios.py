num = int(input('Digite um valor: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} é divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO') 
else: 
    print('Por isso ele NÃO É PRIMO')