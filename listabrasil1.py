print("10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")

tempcel= float(input("Digite a temperatura em graus Celsius:"))
print(((tempcel * 1.8)+32))


print("---------------------------------------------------------------------------------------------------------")


print("11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:o produto do dobro do primeiro com metade do segundo .a soma do triplo do primeiro com o terceiro.o terceiro elevado ao cubo.")

numint1= int(input("Digite um número inteiro:"))
numint2= int(input("Digite um número inteiro:"))
numreal= int(input("Digite um número real:"))

print((((numint1*2)+(numint2/2))) , ((numint1*3)+(numreal)), (numreal**3) )


print("---------------------------------------------------------------------------------------------------------")

print("12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")

altura=float(input("Digite a sua altura:"))
print((72.7*altura) - 58)

print("---------------------------------------------------------------------------------------------------------")

print("13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7")

h=float(input("Digite a sua altura:"))
m = (72.7*h) - 58
f = (62.1*h) - 44.7
print("Com a sua altura e sendo do sexo masculino seu peso ideal é: "  (m))
print("Com a sua altura e sendo do sexo feminino seu peso ideal é: "  (f))

print("---------------------------------------------------------------------------------------------------------")

print("14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas." )

pesodepeixe = float(input("Digite o peso: "))
multa = 4
pesomax = 50
if(pesodepeixe > 50):
    excesso = pesodepeixe - pesomax 
    print("O peso em excesso é: ", excesso)
    print("O valor da multa por excesso é R$", excesso * multa)
else:
        print("Não tem peso em excesso")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:")


valorhora=float(input("Digite o valor recebido por hora trabalhada: R$"))
quanthora=float(input("Digite a quantidade de horas trabalhadas por mês: "))
salbruto = valorhora * quanthora
ir = salbruto * 0.11
inss = salbruto * 0.08
sindicato = salbruto * 0.05
descontos =  ir + inss + sindicato 
salliquido = salbruto - ir - inss - sindicato 


print ("O seu Salário Bruto é R$: ", salbruto)
print ("O seu Imposto de Renda é R$: ", ir)
print ("O seu desconto do INSS é R$: ", inss)
print ("O seu desconto de Sindicato é R$: ",sindicato)
print ("O total de descontos no mês vigente é R$: ", descontos)
print ("O seu Salário Liquido é R$: ", salliquido)


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.")

metros= float(input("Digite a quantidade de M2 a ser pintada: "))
cobertura = (metros / 3.0)
quantilatas = int(cobertura / 18.0)
if( cobertura % 18.0 != 0 ):
    totlatas = quantilatas + 1

print("A quantidade de latas a ser comprada é: ", totlatas )
print("O valor total da compra é: ", totlatas * 80)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o  desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.")

metros= float(input("Digite a quantidade de M2 a ser pintada: "))

cobertura = ((metros / 6.0) * 0,10) #6.0 é igual capacidade de um litro de tinta.

latas = float(cobertura / 18.0)

galao = float(cobertura / 3.6)

quantilatas = int(cobertura / 18.0)
quantigalao = int(galao / 3.6)
if( cobertura % 18.0 != 0 ):
    totlatas = latas + 1
if(cobertura % 3.6 != 0):
    totgalao = galao + 1


print("A quantidade de latas a ser comprada é: ", totlatas )
print("A quantidade de galões a ser comprada é: ", totgalao )
print("O valor total da compra é: ", totlatas * 80)
print("O valor total da compra é R$: ", totgalao * 25)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). ")


#1 Byte = 8 bits

#1 kilobyte (KB ou Kbytes) = 1024 bytes

#1 megabyte (MB ou Mbytes) = 1024 kilobytes



tamanho = int(input("Digite um valor: "))
velo = int(input("Digite a velocidade: "))

mb = tamanho * 1024 *  1024 * 8 
conexao = mb / velo # velocidade em megabits
minuto  =  conexao / 60 # velocidade dividida pelo tempo de 1m

print('Tempo aproximado de download:', minuto, 'm')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
