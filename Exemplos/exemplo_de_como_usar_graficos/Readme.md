# README: Visualização de Gráficos com Matplotlib em Python

Este documento oferece instruções e informações sobre dois scripts Python que demonstram a criação de gráficos utilizando a biblioteca Matplotlib. O primeiro script cria um gráfico de linha simples, enquanto o segundo gera um gráfico com duas equações de segundo grau.

## Descrição

Matplotlib é uma biblioteca de visualização de dados em Python que permite a criação de uma ampla variedade de gráficos e plots estáticos, animados e interativos. Neste README, cobrimos dois exemplos: um gráfico de linha básico e um gráfico que ilustra duas equações de segundo grau.

## Pré-requisitos

Para executar esses scripts, você precisará ter Python instalado em seu sistema, juntamente com a biblioteca Matplotlib. Se você não tiver o Matplotlib instalado, pode adicioná-lo usando o gerenciador de pacotes pip com o comando `pip install matplotlib`. Para o segundo script, também é necessário ter a biblioteca NumPy, que pode ser instalada com `pip install numpy`.

## Estrutura dos Códigos

### Gráfico de Linha Simples

O primeiro script cria um gráfico de linha básico usando coordenadas especificadas:

- Importação da biblioteca Matplotlib.
- Definição dos dados dos eixos X e Y.
- Criação do gráfico de linha.
- Adição de rótulos e título.
- Exibição do gráfico.

### Gráfico de Equações de Segundo Grau

O segundo script gera um gráfico com duas equações de segundo grau:

- Importação das bibliotecas NumPy e Matplotlib.
- Geração de valores para o eixo X.
- Cálculo dos valores de Y para duas equações de segundo grau.
- Plotagem das duas equações no gráfico.
- Adição de rótulos, título, grade e legenda.
- Exibição do gráfico.

## Códigos

### Gráfico de Linha Simples

```python
import matplotlib.pyplot as plt

# Dados do gráfico
x = [-3, 0]
y = [0, 1]

# Criar o gráfico de linha
plt.plot(x, y)

# Adicionar rótulos aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Adicionar um título ao gráfico
plt.title("Gráfico de Linha")

# Exibir o gráfico
plt.show()
```

### Gráfico de Equações de Segundo Grau

```python
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
```

## Executando os Scripts

1. Salve cada trecho de código em um arquivo `.py` separado.
2. Execute os arquivos em um ambiente Python.
3. Os gráficos correspondentes serão exibidos em janelas separadas.

## Conclusão

Estes scripts são exemplos práticos de como utilizar a biblioteca Matplotlib para visualizar dados e funções matemáticas em Python. Eles servem como uma introdução básica à plotagem de gráficos e podem ser expandidos para visualizações mais complexas e personalizadas.
