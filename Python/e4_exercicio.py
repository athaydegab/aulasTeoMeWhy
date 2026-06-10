# garrafa de agua

apresentacao = """
Olá, seja bem-vindo à loja de água mineral!
Escolha o que deseja comprar:
1. Água Mineral Natural - R$ 2,50
2. Água Mineral com Gás - R$ 3,00
"""

print(apresentacao)
valor_item = 0
qtde = 0

escolha = input("Escolha:")

if escolha == "1":
    print("Você escolheu a Água Mineral Natural. Ótima escolha!")

elif escolha == "2":
    print("Você escolheu a Água Mineral com Gás. Ótima escolha!")

if escolha == "1":
    valor_item = 2.50
elif escolha == "2":
    valor_item = 3.00 



if valor_item == 0:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

else:
    qtde = input("Quantas garrafas você deseja comprar? ")
    qtde = int(qtde)
    conta = valor_item * qtde
    print(f"O total da sua compra é: R${conta:.2f}")