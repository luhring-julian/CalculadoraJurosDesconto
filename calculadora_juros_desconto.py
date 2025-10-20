#=========================================
# Calculadora de Juros Simples e Descontos
# Desenvolvida para reforçar os conhecimentos adquiridos no Bootcamp LuizaLabs
#=========================================

print("=== CALCULADORA DE JUROS SIMPLES E DESCONTO ===")
print("Vamos calcular juros simples e um valor de desconto a partir de um valor base!\n")

preco_base = float(input("Digite o valor base em R$: "))
desconto_percentual = float(input("Digite o valor do desconto em %: "))
taxa_juros_percentual = float(input("Digite a taxa de juros em %: "))
periodo = int(input("Digite o período que os juros irão incidir (em meses): "))

# Conversões de percentuais para decimais
desconto = desconto_percentual / 100
juros = taxa_juros_percentual / 100


# Cálculo do valor com desconto
valor_desconto = preco_base * desconto
preco_com_desconto = preco_base
preco_com_desconto -= valor_desconto

# Cálculo do valor com juros simples
valor_juros = preco_base * juros * periodo
preco_com_juros = preco_base
preco_com_juros += valor_juros

# Exibição dos resultados
print("\n=== RESULTADOS ===")
print(f"Valor do desconto: R$ {valor_desconto}")
print(f"Preço com o desconto aplicado: R$ {preco_com_desconto}")
print(f"Valor dos juros: R$ {valor_juros}")
print(f"Preço com os juros aplicados: R$ {preco_com_juros}")