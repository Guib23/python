qtde=int(input("Digite a qtde de maças:"))

if qtde<12:
    precoTotal=1.30 * qtde
else:
    precoTotal=1.00 * qtde

print(qtde, " maça(s) são vendidas por ",format(precoTotal, '.2f'))