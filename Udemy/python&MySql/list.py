x = [1, 2, 3, 4, 5]
y = []

# for i in x:
#     y.append(i**2)

# print(x)
# print(y)

# usando list comprehension
# y [valor_a_adicionar laço e conição]
y = [i**2 for i in x]

print(x)
print(y)


z = [i for i in x if i%2 == 1]

print(z)