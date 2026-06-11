# %%
numero = 2
count = 0

while count < 101:
    print(numero, "x", count, "=", numero * count)
    count += 1

# %%
soma = 0
qtde_entradas = 4

while qtde_entradas > 0:
    altura = float(input("Digite sua Altura: "))
    soma += altura
    qtde_entradas -= 1

print("A soma dos números é:", soma)



# %%
saldo_total = 0

while True:
    saldo = input("Digite o saldo:")
    
    if saldo == "":
        break # Termina o laço na linha do Break
    
    saldo_total += float(saldo)

print(saldo_total)
