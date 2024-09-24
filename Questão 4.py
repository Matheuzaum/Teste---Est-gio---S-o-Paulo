# Dicionário com o faturamento de cada estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total de faturamento
faturamento_total = sum(faturamento_estados.values())

# Calcula e exibe o percentual de representação de cada estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
