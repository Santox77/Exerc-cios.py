pesomaior = 0
pesomenor = 0
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}° pessoa:"))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else: 
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print("O maior peso é: {}".format(pesomaior))
print("O menor peso é: {}".format(pesomenor))
