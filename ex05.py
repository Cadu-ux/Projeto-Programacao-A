print("Digite 10 números:")
numeros = [int(input()) for _ in range(10)]

ultimo_numero = numeros[-1]
# Conta quantas vezes o último número aparece no array inteiro
ocorrencias = numeros.count(ultimo_numero)

print(f"\nO último número lido foi {ultimo_numero} e ele ocorreu {ocorrencias} vez(es).")