# Listas tem Elementos Mutáveis, ou seja, podem ser alterados depois de criados. São representados por colchetes [].
# Pode-se colocar qualquer tipo de dado dentro de uma lista, inclusive outras listas.
# Listas não são arrays, ou seja, não possuem as mesmas funcionalidades de um array, como por exemplo, operações matemáticas. Para isso, existe a biblioteca Numpy. 
# %%

idades = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100]


# %%

teo = ["Teo", 20, "Masculino", "Programador", 1.80, ["Python", "Java", "C++"]]
print(teo)
type(teo)
# %%

# idade
print(teo[1])

# sexo
print(teo[2])

# linguagem de programação
print(teo[5])
# %%

idades = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100]

# soma das idades
sum(idades)

# media das idades
sum(idades) / len(idades)

# %%
