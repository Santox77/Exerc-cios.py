sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input("Dados invaidos. Por favor informe seu sexo: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))