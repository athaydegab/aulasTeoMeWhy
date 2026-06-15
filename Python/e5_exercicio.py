# %%
lista = [1, 1, 2, 1, 3, 4, 5, 2, 1, 2, 3, 1, 3, 4, 5, 2, 1, 2, 4, 2, 3 ,2 ,1 ,3]

numero = input("Digite um número: ")
numero = int(numero)

contador = 0
for i in lista:
    print(i)
    if i == numero:
        contador += 1

print(f"O número {numero} aparece {contador} vezes na lista.")

# %%
lista.append(10)

print(lista)

# %%

idades = []

while True:
    idade = input("Digite uma idade: ")
    
    if idade == '':
        break

    idades.append(idade)
    
idades = [int(idade) for idade in idades]

print("Idades:", idades)

# %%