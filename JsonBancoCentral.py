import json


with open(r"C:\Users\Intrack Design\Desktop\Python\bc.json") as d:
    dados = json.load(d)

for i in dados:
    print(i)

print("Fim do Programa!")
