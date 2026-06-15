


# %%
idades = [18, 16, 15, 19, 90]

print(idades[0])  # Acessa o primeiro elemento da lista
print(idades[1])  # Acessa o segundo elemento da lista

print("Soma Idade:", sum(idades))

print("Média Idade:", sum(idades) / len(idades))

print("Idade Máxima:", max(idades))
print("Idade Mínima:", min(idades))

#%%

teo = ["Teo Calvo", 
       32, 
       "Engenheiro de Software", 
       ["Ana", "Maria", "João"]]

print(teo[0])  # Acessa o nome
print(teo[1])  # Acessa a idade

teo[3][0]
# acessar filhos
filhos = teo[3]
primeiro_filho = filhos[0]
print(primeiro_filho)

#%%

# acessar ultimo filho
tamanho_lista = len(teo)
posicao_filhos = tamanho_lista - 1
filhos = teo[posicao_filhos]
ultimo_filho = filhos[-1]
print(ultimo_filho)

# ou usa numeros negativos para acessar a partir do final da lista

print(teo[-1][-1])

#%%

idades = [18, 16, 15, 19, 90]


# Intervalo Aberto
print(idades) 

print(idades[1:3])

# [start:stop:step] - 
# start: elemento que se deve começar. 
# stop: elemento que se deve parar (não incluído)
# step: o passo, ou seja, de quantos em quantos elementos se deve avançar

print(idades[-2:]) 

# %%

filhos = teo[3]
filhos[::2]  # Acessa os filhos pulando de 2 em 2

# %%
