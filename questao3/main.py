#Escreva um programa que receba como entrada três números e exiba uma mensagem informando qual é o maior deles. 

a= int(input("informe o primeiro número: "))
b= int(input("informe o segundo número: "))
c = int(input("informe o terceiro número: "))
print("se o maior número for igual a 0 é que foram informados dois números iguais: ")
maior = 0
if a>b and a>c :
 maior = a
elif b>a and b>c:
  maior = b
elif c>a and c>b:
  maior = c
print(f"o maior número é {maior} ")





