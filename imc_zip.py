# Listas de alturas e pesos correspondentes
alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

# Calculando o IMC para cada par de altura e peso
# Utilizando a fórmula do IMC: peso (kg) / (altura (m) ^ 2)
# A função round é usada para arredondar o IMC para uma casa decimal
# zip(alturas, pesos) emparelha cada altura com o correspondente peso, produzindo tuplas (altura, peso).
imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]

# Imprimindo a lista de IMCs calculados
print(imc)

