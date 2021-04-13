#Abrir arquivos - usamos a função Open
# e ha 6 tipos de modo:
# r -> Somente leitura, w -> modo escrito, a -> leitura e escrita, ao fim da linha
# r+ -> leitura e escrita, w+ -> modo escrita(apaga a anterior), a+ -> leitura e escrita(abre arquivo para atualização)

#read() -> lê arquivo
#readline() -> lê uma linha
#readlines() -> lê o arquivo e armazena numa lista

arquivo = open("teste.txt")

# text_completo = arquivo.read()
# print(text_completo)

linhas = arquivo.readlines()
print(linhas)

for l in linhas:
    print(l)


### Criar Arquivo
#encoding: utf-8 -> para poder usar acento
w = open("teste2.txt", "w", encoding="utf-8") #como está 'w' vai criar arquivo novo e substituir o anterior
w.write("Esse é o meu arquivo 2, muito Bom \n")
w.close()

w = open("teste.txt", "a", encoding="utf-8") #como está 'a' vai abrir o arquivo e adicionar a linha ao final
w.write("Esse é o meu arquivo 2 \n")
w.close()
