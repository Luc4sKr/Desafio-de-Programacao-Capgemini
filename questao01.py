def cria_escada(n):
    for i in range(1, n+1):
        print("*" * i)


n = -1
while True: 
    if n < 0:
        n = int(input("Digite um número positivo: "))
    else:
        break

cria_escada(n)