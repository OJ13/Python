a = 1
b = 2
c = 3

d = a + b + c

# print(a)
# print(b)
# print(c)
# print(d)

valorHora=5
dias=30
horaTrabalho=8
salario=valorHora*dias*horaTrabalho
nome="Osmar Junior"

print(valorHora)
print(dias)
print(horaTrabalho)
print(salario)
print(nome)

print(float(valorHora))
print(int(15.8))
print(str(8000))

print(nome[0:5])
print(nome+nome)
print(nome*3)
print("o" in nome)
print("z" in nome)

lista = [1 , 5 , "OJ", True, "Python", 50]
print(lista)
lista.append(False)
print(lista)
lista.append(70)
print(lista)
lista.append(1)
print(lista)

print(lista[5])
print(lista[4])
print(lista.index(50))
print(lista.count("OJ"))

lista.remove(1)
print(lista)

lista.reverse()
print(lista)

lista2 = [9, 7, 12, 505, 2, 25]
lista2.sort()
print(lista2)

telefones = { "rocky": 99885507, "apollo": 87759900, "adonis": 99665577 }
print(telefones)

telefones["polly"]=99997777
print(telefones)

del telefones["adonis"]
print(telefones)

tuplas=("balboa", "udemy", "python")
print(tuplas)
print(tuplas[0])
print(tuplas[0:1])
print(tuplas[0:3])
print(len(tuplas))
print("balboa" in tuplas)

lista.append(tuplas)
print(lista)