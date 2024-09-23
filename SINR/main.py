import json
import matplotlib.pyplot as plt

# Ler o arquivo JSON
with open('data/SINR/teste.json', 'r') as file:
    data = json.load(file)

# Inicializar listas para armazenar potências e valores de SINR
potencias = []
sinr_values = []

# Iterar sobre cada teste
for test_run, test_data in data.items():
    potencia = int(test_data['itervars']['potencia'])
    for scalar in test_data['scalars']:
        if scalar['name'] == 'measuredSinrDl:mean':
            sinr_value = scalar['value']
            potencias.append(potencia)
            sinr_values.append(sinr_value)

# Gerar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(potencias, sinr_values, color='blue')
plt.xlabel('Potência')
plt.ylabel('SINR (dB)')
plt.title('Potência vs Qualidade de Sinal (SINR)')
plt.grid(True)
plt.show()