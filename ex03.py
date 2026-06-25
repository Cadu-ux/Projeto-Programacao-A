def vantagem(candidato, concorrente, n):
    maior_vantagem = 0.00
    
    for i in range(n):
        if candidato[i] > concorrente[i]:
            diferenca = candidato[i] - concorrente[i]
            if diferenca > maior_vantagem:
                maior_vantagem = diferenca
                
    return maior_vantagem

# Lê o tamanho do array
n = int(input())

# Lê os números da mesma linha, separa por espaço e converte todos para float
candidato = list(map(float, input().split()))
concorrente = list(map(float, input().split()))

# Chama a função
resultado = vantagem(candidato, concorrente, n)

# Imprime o resultado formatado com exatas 2 casas decimais
print(f"{resultado:.2f}")