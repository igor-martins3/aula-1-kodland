import random

# Todos os caracteres permitidos para a senha
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Pede para o usuário informar o tamanho da senha
tamanho = int(input("Digite o comprimento desejado da senha: "))

# Variável onde a senha será construída
senha = ""

# Loop para gerar a senha aleatória
for _ in range(tamanho):
    senha += random.choice(caracteres)

# Exibe a senha final
print("Sua senha gerada é:", senha)
