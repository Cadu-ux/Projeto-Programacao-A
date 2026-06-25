n = int(input("Digite a quantidade de notas: "))

print(f"Digite as {n} notas:")
notas = [float(input()) for _ in range(n)]

# Calcula a média (evita divisão por zero)
media = sum(notas) / n if n > 0 else 0

# Calcula os limites (10% acima = media * 1.10, 10% abaixo = media * 0.90)
limite_superior = media * 1.10
limite_inferior = media * 0.90

acima = sum(1 for nota in notas if nota > limite_superior)
abaixo = sum(1 for nota in notas if nota < limite_inferior)

print(f"\nMédia da turma: {media:.2f}")
print(f"Notas mais de 10% acima da média: {acima}")
print(f"Notas menos de 10% abaixo da média: {abaixo}")