#Baskara
#a2 + bx + c
#(-b +- sqtr(b2-4ac))/2
from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %f" %x1)
print("x2 = %f" %x2)

##Ordenar Listas
lista = [5, 9, 3, 2, 1, 8, 0]

#print(sorted(lista)) #função já para isso

#select sort
for i in range(len(lista)):
    menor = i

    for j in range(i+1, len(lista)):

        if lista[j] < lista[menor]:
            menor = j
    
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)


num1 = int(input("Digite o primeiro número: "))
operador = input("Digite o operador: ")
num2 = int(input("Digite o segundo número: "))
resultado = 0

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print("Operador não encontrado")

print(resultado)