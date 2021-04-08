# -*- coding: utf-8 -*-
#primeiro programa
print("Hello World")
print("Quarta feira de manha")
print("mensagem 3")
print("Olá Mundo!")

"""
Comentario
de
 multiplas 

 linhas
"""
### funções matemáticas
print(2 + 2)
print(5 - 3)
print(2 / 2)
print(5 * 5)
print(2 **3) # 2 elevado a 3
print(10 / 3)
print(10 % 3)

### variaveis e dados
var1 = 1        #int
var2 = 5.58     #float
var3 = "OJ"     #string
var4 = True     #boolean

### Operadores lógicos
x = 2
y = 3

if(x == y):
    print("igual")

if(x != y):
    print("difente")

if(x < y):
    print("x é menor que y")

if(x > y):
    print("x é maior que y")

if(x <= y):
    print("x é menor ou igual que y")

if(x >= y):
    print("x é maior ou igual que y")

if(x < y and x != y):
    print("And")

if(x < y or x == y):
    print("Or")

if not x == y:
    print("NOT")

x = 1
y = 2

if x < y:
    print("x menor que y")
elif x == y:
    print("x é igual a y")
else:
    print("y menor que x")

x = 1

while x <= 10:
    print(x)
    x += 1

lista = [1, 2 , 3, 4, 5]
lista2 = ['Ola', 'Tudo bem', 'Bom dia']
lista3 = [True, "correto", 9.88, "São Paulo FC"]

for i in lista:
    print(i)

for i in lista2:
    print(i)

for i in lista3:
    print(i)

for i in range(10, 20, 2):  # de 10 à 20 e de 2 em 2
    print(i)


numero = input("Digite um número: ")
print(numero)

nome = input("Digite seu nome: ")
print("Bem Vindo " + nome)

tamanho = len(nome)
print("Quantidade de Caracteres do nome " + str(tamanho))

print(nome[0])
print(nome[1])
print(nome[0:5])
print(nome.lower())
print(nome.upper())
print(nome.strip())
print(nome.split(" "))
print(nome.find("sma")) #Se ele não encontrar ele retorna -1
print(nome.replace("Osmar", "OJ"))











