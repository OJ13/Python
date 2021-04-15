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

### loops
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

### input output - strings function
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

### listas
list1 = ["aaaa", "bbbb", "cccc"]
list2 = [1,2,3,4,5,6,7,8,9]
list3 = ["abacaxi", 2, 2.89, True]

print("---------------")
print(list1)
print(len(list1)) #verificar tamamnho

list1.append("dddddd")  #add item a lista
print(list1)

if 7 in list2:
    print("7 esta na lista")

del list1[2] #remover item da lista, item na posição 2
print(list1)

del list1[2:] #remover item da lista, 2 em diante
print(list1)

del list1[:] #remover item da lista, lista inteira
print(list1)

list4 = [5, 8, 1, 2, 88, 77, 99, 105, 36, 7, 6]
list4.sort() #ordenar crescente
print(list4)
list4.sort(reverse=True) #ordenar decrescente
print(list4)
list4.reverse() #reversão da lista
print(list4)

### Dicionarios (Dictionary)
meu_dicionario = {"A": "Ameixa", "B": "Bola", "C": "Cachorro"}
print(meu_dicionario)
print(meu_dicionario["A"])

for chave in meu_dicionario:
    print(chave + " - " + meu_dicionario[chave])

for i in meu_dicionario.items():
    print(i)

for i in meu_dicionario.keys():
    print(i)

for i in meu_dicionario.values():
    print(i)


### Gerando numeros aleatorios
import random

numero = random.randint(0, 10) #randint escolhe um randomico entre 0 e 10
print(numero)

lista = [25, 47, 9, 8]
numero = random.choice(lista) #choice - escolhe algum item da lista
print(numero)









