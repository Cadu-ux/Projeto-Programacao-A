print("Digite 101 números inteiros:")
numeros = [int(input()) for _ in range(101)]

# O último número é o alvo
ultimo_numero = numeros[-1]
# Os primeiros 100 números onde faremos a busca
primeiros_100 = numeros[:100]

# Armazena os índices em que o número aparece
posicoes = [i for i, valor in enumerate(primeiros_100) if valor == ultimo_numero]

if posicoes:
    print(f"\nO número {ultimo_numero} está presente nas seguintes posições: {posicoes}")
else:
    print(f"\nO número {ultimo_numero} não está presente nos 100 primeiros números.")