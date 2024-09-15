import json
import matplotlib.pyplot as plt

# Nesse arquivo o objetivo é obter, de acordo com a potência, a soma total de vazão de cada teste. 
# Para isso, é necessário ler o arquivo JSON e iterar sobre cada teste, obtendo a potência e a soma total de vazão.
# Por fim, é gerado um gráfico de barras com a potência no eixo x e a soma total de vazão no eixo y.

# Ler o arquivo JSON
with open('data/teste2.json', 'r') as file:
    data = json.load(file)

# Inicializar listas para armazenar potências e somas de vazão
potencias = []
somas_vazao = []

# Iterar sobre cada teste
for test_run, test_data in data.items():
    potencia = int(test_data['itervars']['potencia'])
    total_vazao = sum(scalar['value'] for scalar in test_data['scalars'])
    
    potencias.append(potencia)
    somas_vazao.append(total_vazao * 8 / 1000000)  # Multiplicar por 8 e dividir por 1000000 (para converter de bytes para megabits(Mbps))

# Gerar o gráfico em formato de barras
plt.figure(figsize=(10, 6))
plt.bar(potencias, somas_vazao, color='blue')
plt.xlabel('Potência')
plt.ylabel('Vazão Total (Mbps)')
plt.title('Potência vs Total de Vazão')
plt.grid(True)
plt.show()