n = int(input())

array = list(map(int, input().split()))
menor_elemento = min(array)
posicao = array.index(menor_elemento) + 1

print(f"{menor_elemento}")
print(f"{posicao}")