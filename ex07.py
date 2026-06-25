n = int(input("Digite o tamanho do array: "))

print(f"Digite os {n} números:")
array = [int(input()) for _ in range(n)]

# a) Ordem inversa
ordem_inversa = array[::-1]

# b) Deslocamento para a esquerda (tira o 1º elemento e coloca no final)
if n > 0:
    deslocamento_esquerda = array[1:] + [array[0]]
else:
    deslocamento_esquerda = []

# c) Ordenado em ordem decrescente
ordem_decrescente = sorted(array, reverse=True)

print(f"\na) Ordem inversa: {ordem_inversa}")
print(f"b) Deslocamento para a esquerda: {deslocamento_esquerda}")
print(f"c) Ordem decrescente: {ordem_decrescente}")