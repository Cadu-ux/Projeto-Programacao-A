print("Digite a sequência de números positivos (0 para terminar):")
maior_numero = 0

while True:
    numero = int(input())
    if numero == 0:
        break
    
    if numero > maior_numero:
        maior_numero = numero

if maior_numero > 0:
    print(f"\nO maior número digitado foi: {maior_numero}")
else:
    print("\nNenhum número válido foi digitado antes do 0.")