print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("1. Faça um Programa que peça dois números e imprima o maior deles.")

n1= int(input("Digite um número:"))
n2= int(input("Digite um número:"))
if (n1 > n2):
    print(n1)
else:
    print(n2)


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.")

n1= int(input("Digite um número:"))
if (n1 <= -1):
    print(n1)
else:
    print(n1)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")

letra = input("Digite a letra identificadora de genero: ")
if (letra == "M" ):
    print("MASCULINO")
elif(letra == "F"):
    print("FEMININO")
else:
    ("Genero não identificado")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")

letra = input("Digite uma letra: ")
if (letra == "a","e","i","o","u" ):
    print("VOGAL")
else:
    print("CONSOANTE")


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez."

nota1= float(input("Digite a primeira nota do aluno: "))
nota2= float(input("Digite a segunda nota do aluno: "))
media= ((nota1+nota2)/2)
print(media)
if(media == 10.0):
    print("Aluno Aprovado com Distinção!")
elif(media >= 7.0):
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("6. Faça um Programa que leia três números e mostre o maior deles.")


num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))
num3= float(input("Digite o terceiro número: "))
if(num1 > num2) or (num1 > num3):
    print(num1)
elif(num2 > num3) or (num2 > num3):
    print(num2)
elif(num2 > num3) or (num2 > num3):
    print(num3)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("7. Faça um Programa que leia três números e mostre o maior e o menor deles.")


#REVER

num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))
num3= float(input("Digite o terceiro número: "))


if(num1 > num2) or (num1 > num3):
    print(num1)
elif(num2 > num3) or (num2 > num3):
    print(num2)
elif(num2 > num3) or (num2 > num3):
    print(num3)





print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.")

#precisa rever

item1= float(input("qual o preço do produto: "))
item2= float(input("qual o preço do produto: "))
item3= float(input("qual o preço do produto: "))
if(item1 > item2) or (item1 > item3):
    print("O valor do item mais barato é: ", item1)
elif(item2 > item1) or (item2 > item3):
    print("O valor do item mais barato é: ", item2)
elif(item3 > item1) or (item3 > item2):
    print("O valor do item mais barato é: ", item3)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("9. Faça um Programa que leia três números e mostre-os em ordem decrescente.")


num1= float(input("Digite um número: "))
num2= float(input("Digite um número: "))
num3= float(input("Digite um número: "))
print(num3,num2,num1)


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.")


turno = input("Digite M para matutino: ")
if (turno == "M") :
    print("Matutino")
elif (turno  == "V"):
    print("Vespertino")
elif(turno  == "N"):
    print("Noturno")
else:
    ("Valor Invalido")


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.")

#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

sal=float(input("Digite o valor do salario R$: "))
if (sal <= 280):
    aumento = 20
elif(sal <= 700):
    aumento = 15
elif(sal <= 1500):
    aumento = 15
else:
    aumento = 5

acrescimo = sal * (aumento / 100)
novosal = sal + aumento

print ("Salario antes do reajuste:", sal)
print ("Percentual de aumento:", aumento, '%')
print ("Valor do aumento:", acrescimo)
print ("Novo Salario:", novoSal)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.")

hora=float(input("Digite o valor recebido por hora trabalhada R$: "))

quanthoras=float(input("Digite a quantidade de horas trabalhadas R$: "))

salbruto= hora * quanthoras

if (salbruto <= 1500):
    desc = 5
elif(salbruto <= 2500):
    desc = 10
elif(salbruto > 2500):
    desc = 20
elif(salbruto == 900):
    print("ISENTO")

ir = salbruto * (desc / 100)

sindi = salbruto * (3/100)

fgts = salbruto * (11 / 100.0)

inss = salbruto * (10 / 100.0)

totdesc = salbruto - ir - sindi - fgts

liqui = salbruto - totdesc

print ("Salário bruto:", salbruto)
print ("Salário com desconto de IR:", ir)
print ("Salário com desconto de INSS:", inss)
print ("Salário com desconto de FGTS:", fgts)
print ("Salário com desconto do Sindicato:", sindi)
print ("Salário com desconto do Sindicato:", totdesc)
print ("Salário Liquido:", liqui)






