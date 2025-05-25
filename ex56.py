maior_idade = 0 
mulher_com_menos_de_20 = 0
soma_idade = 0
nome_mais_velho = ''
for c in range(1, 5):
    print("---- {}ª PESSOA ----".format(c))
    nome = str(input("NOME: ")).strip()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO F/M: ")).strip().upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulher_com_menos_de_20 += 1
media = soma_idade / 4
print("A media de idade do grupo é {:.1f}".format(media))
if nome_mais_velho:
    print("O nome do homem mais velho do grupo é {} e ele tem {} anos".format(nome_mais_velho, maior_idade))
else:
    print("Não há homens no grupo")
print("A quantia de mulheres com menos de 20 anos é {}".format(mulher_com_menos_de_20))

