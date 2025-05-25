largura = 50
print('='*largura)
print('10 TERMOS DE UMA PA'.center(largura))
print('='*largura)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(' {}'.format(c),end = ' -')
print(' ACABOU')