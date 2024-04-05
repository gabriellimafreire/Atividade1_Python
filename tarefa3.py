import random #importacao

# Gera um numero aleatorio entre 0 e 10
num_ale = random.randint(0, 10)

# Classifica o numero gerado
if num_ale <= 2:
    classificacao = "ruim"
elif num_ale <= 5:
    classificacao = "regular"
elif num_ale <= 8:
    classificacao = "bom"
else:
    classificacao = "ótimo"

# Exibe o numero gerado e sua classificacao
print("Número aleatório:", num_ale)
print("Classificação:", classificacao)
