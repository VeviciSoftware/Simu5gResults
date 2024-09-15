import json
import matplotlib.pyplot as plt

# Ler o arquivo JSON
with open('data/SINR/teste.json', 'r') as file:
    data = json.load(file)

# Inicializar listas para armazenar potências e somas de vazão
potencias = []
somas_vazao = []

# Iterar sobre cada teste
for test_run, test_data in data.items():
    potencia = int(test_data['itervars']['potencia'])
    total_vazao = sum(scalar['value'] for scalar in test_data['scalars'])
    
    potencias.append(potencia)
    somas_vazao.append(total_vazao)
    media_vazao = sum(somas_vazao) / len(somas_vazao)   # Média 

# Gerar o gráfico em formato de barras
plt.figure(figsize=(10, 6))
plt.bar(potencias, media_vazao, color='blue')
plt.xlabel('Potência')
plt.ylabel('Vazão Total (Mbps)')
plt.title('Potência vs Média de Vazão')
plt.grid(True)
plt.show()

