### Comparando Sequencias
import re
seq = input("Digite a sequencia 1: ")
seq2 = input("Digite a sequencia 2: ")

# if(seq == seq2):
#     print("Sequencias Iguais")
# else:
#     print("Sequencias Diferentes")
busca = re.match(seq, seq2)

if busca:
    print("Sequencias identicas")
    print(busca.group())
else:
    print("Sequencias distintas")

###----------------------
### Abrindo um arquivo e lendo
nome = input("Digite o nome do arquivo que você deseja abrir: ")
arquivo = open(nome, encoding='utf8')

linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip()) #strip - retira caracteres especial ao final

###----------------------
### Abrindo um arquivo e lendo
sequencia = input("Digite uma sequencia: ")
arquivo = open("teste3.txt", "w", encoding="utf-8")
arquivo.write(sequencia)
print("Sequencia inserida com sucesso")













