frase = str(input("Digite a frase:")).strip().upper()
seperacao = frase.split()
# junto =''.join(seperacao)
inverso =''
for letras in range(len(frase)-1, -1, -1):
    inverso += frase[letras]
print("Você digitou essa frase {} e  o inverso dela é {}".format(frase, inverso))
if inverso == frase:
    print("É um palimdromo!")
else:
    print("Não é um palindromo!")

