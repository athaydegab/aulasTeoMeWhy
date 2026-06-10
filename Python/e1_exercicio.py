print("Bom dia, Mundo!")


def receber():
    nome = input("Digite seu nome: ")
    return "Olá, " + nome + " seja bem-vindo ao curso de Python!"

mensagem_boas_vindas = receber()

# Exibe a variável no terminal
print(mensagem_boas_vindas)