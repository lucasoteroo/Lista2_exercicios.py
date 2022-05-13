#Escreva um programa que receba como entrada um número e exiba uma mensagem informando se ele é positivo, negativo ou neutro.
#Lembrete: Os números maiores que zero são chamados de positivos, enquanto os números menores que zero são os negativos. Zero é um número neutro.

num = int(input("Informe o número desejado: "))

if num > 0 :
  print("O número informado é positivo: ")
if num == 0 :
  print("o número informado é neutro: ")
if num < 0 :
  print("O número informado é negativo")