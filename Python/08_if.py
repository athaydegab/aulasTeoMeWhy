'''
Condicionais recebem valores booleanos (True ou False) 
e executam blocos de código com base nessas condições.

if é a estrutura condicional mais básica, 
que executa um bloco de código se a condição for verdadeira.

elif é uma abreviação de "else if" e permite verificar múltiplas condições.
elif é diferente de if porque é avaliado somente se a condição do if anterior for falsa.
O que economiza tempo de processamento, pois não precisa avaliar todas as condições se uma delas já for verdadeira.
'''

# %%
idade = 15

if idade >= 18:
    print("Você já pode beber álcool legalmente.")

if idade >= 16:
    print("Você pode dirigir, mas não pode beber álcool legalmente.")

if idade < 16:
    print("Você ainda não pode beber álcool legalmente nem dirigir.")

#%%
idade = 19

if idade >= 18:
    print("Você já pode beber álcool legalmente.")

elif idade >= 16:
    print("Você pode dirigir, mas não pode beber álcool legalmente.")

else:
    print("Você ainda não pode beber álcool legalmente nem dirigir.")
    
#%%
idade = 90

if idade >= 70:
    print("Você não deve beber álcool.")

elif idade >= 18:
    print("Você já pode beber álcool legalmente.")

elif idade >= 16:
    print("Você pode dirigir, mas não pode beber álcool legalmente.")

else:
    print("Você ainda não pode beber álcool legalmente nem dirigir.")
# %%
