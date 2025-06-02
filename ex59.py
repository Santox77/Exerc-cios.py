n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
while True:
    print("=-=" * 10)
    print ("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros 
[ 5 ] sair do programa""")
    opcao = int(input("Qual a sua opção ? "))
    if opcao == 1:
        conta = n1 + n2
        print("A soma de {} + {} é igual a {}".format(n1, n2, conta))
    elif opcao == 2:
        conta = n1 * n2
        print("A multiplicação entre {} * {} é igual a {}".format(n1, n2 , conta))
    elif opcao == 3:
        if n1 > n2:
            print("Entre {} e {} o maior valor é {}.".format(n1, n2, n1))
        elif n2 > n1:
            print("Entre {} e {} o maior valor é {}.".format(n1, n2, n2))
        else:
            print('Os valores sao iguais.')
    elif opcao == 4:
        print("Informe novamente os numeros")
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite um numero: "))
    elif opcao == 5:
        print("Finalizando...")
        break
    else:
        print("Opção invalida. Tente novamente")
print("=-=" * 10)
print("Fim do programa! Volte sempre! ")
