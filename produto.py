
produto=float(input("Digite o valor do produto:"))

if produto<=20.0:
    venda=produto+(0.45*produto)
else:
    venda=produto+(0.30*produto)

print(format(produto, '.2f'), " será vendido por ", format(venda, '.2f'))