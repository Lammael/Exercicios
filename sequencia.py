#a)
n1 = 0

while n1 < 10:
    if n1 % 2 == 0:
        pass
    else:
        print(n1)
    n1 += 1
print("-" * 20)

#b)
numero = 1

while numero < 200:
    print(numero)
    numero *= 2
print("-" * 20)

#c)
lista = list()

for i in range(1, 11):
    lista.append(i**2)
print(lista)
print("-" * 20)

#d)
lista = list()

for i in range(11):
    if i % 2 == 0:
        lista.append(i**2)
print(lista)
print("-" * 20)

#e)
nterms = 8
n1, n2 = 0, 1
count = 0

while count < nterms:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count +=1
print("-" * 20)

#f) Não saberia programar esse, mas a resposta seria 200, pois é uma sequência onde todos números começam com "D"


    




