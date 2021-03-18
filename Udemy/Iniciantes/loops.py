for x in range(0, 5) :
    print("valor de x é ",x)

print("-------------")

for x in range(1, 5) :
    print("valor de x é ",x)

print("-------------")

nome="Osmar"
for letra in nome:
    print(letra)

print("------------")

lista=["Rocky", 1999, "Balboa"]
for valor in lista:
    print(valor)

print("-------------")
numero = 15
while (numero > 0):
    print("numero: ", numero)
    numero = numero - 1

print("------------")
numero = 20
while True:
    numero = numero -1
    print("numero é: ", numero)
    if (numero == 2):
        break

numero = 10
while True:
    numero =  numero - 1
    if (numero == 4):
        print("passou no continue")
        continue
    print(numero)
    if (numero == 2):
        break

print("--------------")
for x in range(0,5):
    pass
    