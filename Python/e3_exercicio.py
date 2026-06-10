numero = input("Digite um número: ")

print("O número digitado foi:", numero, "e o tipo do dado é:", type(numero))

numero = int(numero)
raiz = numero ** (1/2)

if raiz % 1 == 0:
    raiz = int(raiz)

print("A raiz quadrada de", numero, "é", raiz)