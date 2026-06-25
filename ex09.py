cpf = input("Digite o CPF (XXX.YYY.ZZZ-DD): ")

# Substitui o '-' por '.' para ter um separador padrão, e divide a string
cpf_formatado = cpf.replace("-", ".")
partes_cpf = cpf_formatado.split(".")

print("\nPartes do CPF:")
for parte in partes_cpf:
    print(parte)