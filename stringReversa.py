palavra = str(input("Digite uma frase: "))
nova_palavra = ""

for i in range(len(palavra)-1, -1, -1):
    nova_palavra += palavra[i]
print(nova_palavra)