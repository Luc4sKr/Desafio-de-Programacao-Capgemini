senha = input("Digite uma senha: ")

caracteres_especiais = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-")
minimo_caractere = tem_digito = tem_minusculo = tem_maiusculo = tem_caractere_especial = False

if len(senha) >= 6:
    minimo_caractere = True

for i in range(len(senha)):
    if senha[i].isdigit():
            tem_digito = True
    if senha[i].islower():
        tem_minusculo = True
    if senha[i].isupper():
        tem_maiusculo = True

    for j in range(len(caracteres_especiais)):
        if senha[i] == caracteres_especiais[j]:
            tem_caractere_especial = True


print("Minimo de caracteres: ", end="")
if minimo_caractere:
    print("ok")
else:
    print(f"faltam {6 - len(senha)} caraceres")
        
print("Contém um digito: ", end="")
if tem_digito:
    print("sim")
else:
    print("não")

print("Contém uma letra minúscula: ", end="")
if tem_minusculo:
    print("sim")
else:
    print("não")

print("Contém uma letra maiúscula: ", end="")
if tem_maiusculo:
    print("sim")
else:
    print("não")

print("Contém caracteres especiais: ", end="")
if tem_caractere_especial:
    print("sim")
else:
    print('não')
    