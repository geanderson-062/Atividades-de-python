# exemplo de grafico com a equação de segundo grau

import numpy as np
import matplotlib.pyplot as plt

# Gerar valores para o eixo x
x = np.linspace(-10, 10, 100)

# Calcular os valores correspondentes no eixo y para a primeira equação
y1 = x**2 + 6 * x

# Calcular os valores correspondentes no eixo y para a segunda equação
y2 = 2 * x - 3

# Plotar o gráfico das equações
plt.plot(x, y1, label="y = x^2 + 6x")
plt.plot(x, y2, label="y = 2x - 3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico das Equações")
plt.grid(True)
plt.legend()
plt.show()
