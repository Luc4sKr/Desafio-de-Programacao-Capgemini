import collections

def anagrama(string):
    comparacao = lambda x, y: collections.Counter(x) == collections.Counter(y)

    tam_anagrama = 1
    tam = len(string)
    lista_palavras = list(string)
    count = 0

    while tam_anagrama < tam:
        total_anagrama = tam - tam_anagrama
        for i in range(total_anagrama):
            palavra1 = ""
            c = 0
            while c < tam_anagrama:
                palavra1 = palavra1 + lista_palavras[i+c]
                c+=1

            for j in range(total_anagrama-i):
                palavra2 = ""
                c = 1
                while c <= tam_anagrama:
                    palavra2 = palavra2 + lista_palavras[j+i+c]
                    c += 1
                p1 = list(palavra1)
                p2 = list(palavra2)

                if comparacao(p1, p2) == True:
                    count += 1
        tam_anagrama += 1

    return count

print(anagrama("ifailuhkqq"))