n = int(input("Digite o tamanho do array: "))

print(f"Digite os {n} números:")
array = [int(input()) for _ in range(n)]

# Acha o menor elemento e seu índice
menor_elemento = min(array)
posicao = array.index(menor_elemento)

print(f"\nMenor elemento: {menor_elemento}")
print(f"Posição: {posicao}")