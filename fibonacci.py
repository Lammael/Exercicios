nterms = int(input("Digite um número: "))
n1, n2, n3 = 0, 1, 0

while nterms > n3 :
    n3 = n1 + n2
    n1 = n2
    n2 = n3

if n3 == 0 or n3 == 1:
    print(f"O número {nterms} faz parte da sequência fibonacci")
elif nterms == n3:
    print(f"O número {nterms} faz parte da sequência fibonacci")
else:
    print(f"O número {nterms} não faz parte da sequência fibonacci")


