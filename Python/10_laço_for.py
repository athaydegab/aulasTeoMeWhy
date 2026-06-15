# FOR é para percorrer elementos
# WHILE é para 

# %%

nome = "gabriel"

# letra é uma variavel temporária, só existindo no laço
for letra in nome:
    print(letra)

# %%
numero = 2
max_numero = 100

# range é uma estrutura de dados que cria uma sequencia de números
# range(número inicial, numero final)

for i in range(1, max_numero + 1):
    print(numero, "x", i, "=", numero * i)

# %%

for i in range(4, max_numero + 1):
    if i % 4 == 0:
        print(i)
    
# %%
soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = float(input("Digite sua Altura: "))
    soma += altura

print("Soma das Alturas: ", soma)