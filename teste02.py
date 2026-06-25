m3 = float(input())
custo_litro = float(input())
litros = m3 * 1000
valor_agua = litros * custo_litro
valor_esgoto = valor_agua * 0.80
valor_total = valor_agua + valor_esgoto
print(valor_agua)
print(valor_esgoto)
print(valor_total)