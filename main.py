import json
import matplotlib.pyplot as plt

# Ler o arquivo JSON
with open('teste2.json', 'r') as file:
    data = json.load(file)

# Inicializar listas para armazenar potências e médias de vazão
potencias = []
medias_vazao = []

# Iterar sobre cada teste
for test_run, test_data in data.items():
    potencia = int(test_data['itervars']['potencia'])
    num_ue = int(next(config['*.numUe'] for config in test_data['config'] if '*.numUe' in config))
    total_vazao = sum(scalar['value'] for scalar in test_data['scalars'])
    media_vazao = total_vazao / num_ue
    
    potencias.append(potencia)
    medias_vazao.append(media_vazao)

# Gerar o gráfico em formato de barras
plt.figure(figsize=(10, 6))
plt.bar(potencias, medias_vazao, color='blue')
plt.xlabel('Potência')
plt.ylabel('Média de Vazão (Bps)')
plt.title('Potência vs Média de Vazão')
plt.grid(True)
plt.show()