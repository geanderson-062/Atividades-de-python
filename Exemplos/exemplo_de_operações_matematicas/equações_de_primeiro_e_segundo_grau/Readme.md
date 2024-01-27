# README para Códigos de Equações de Primeiro e Segundo Grau

Este documento oferece uma explicação detalhada sobre dois scripts Python que resolvem equações de primeiro e segundo grau, utilizando a biblioteca `sympy`. Estes scripts são particularmente úteis para fins educacionais, demonstrando como a programação pode ser aplicada na resolução de problemas matemáticos.

## Dependências

Para executar estes scripts, é necessário ter a biblioteca `sympy` instalada. Se você ainda não tem esta biblioteca, pode instalá-la usando pip:

```bash
pip install sympy
```

## Uso

### 1. Equação de Primeiro Grau

O primeiro script resolve uma equação linear (de primeiro grau) da forma `ax + b = c`.

#### Código:

```python
from sympy import symbols, Eq, solve

# Definir o símbolo
x = symbols('x')

# Definir a equação
equacao = Eq(2*x + 4, 10)

# Resolver a equação
solucao = solve(equacao, x)

print(solucao)  # O resultado será [3]
```

#### Explicação:

- `symbols('x')`: Define 'x' como um símbolo matemático.
- `Eq(2*x + 4, 10)`: Cria uma equação do tipo 2x + 4 = 10.
- `solve(equacao, x)`: Resolve a equação em relação a 'x'.
- `print(solucao)`: Exibe a solução da equação, que neste caso é [3].

### 2. Equação de Segundo Grau

O segundo script resolve uma equação quadrática (de segundo grau) da forma `ax^2 + bx + c = dx + e`.

#### Código:

```python
from sympy import symbols, Eq, solve

# Definir o símbolo
x = symbols('x')

# Definir a equação
equacao = Eq(x**2 + 6*x, 2*x - 3)

# Resolver a equação
solucao = solve(equacao, x)

print(solucao)  # O resultado será [-3, -1]
```

#### Explicação:

- `Eq(x**2 + 6*x, 2*x - 3)`: Define uma equação do tipo x² + 6x = 2x - 3.
- O resto do processo é similar ao script de primeiro grau, resolvendo a equação e exibindo as soluções. Neste caso, as soluções são [-3, -1], pois é uma equação quadrática que pode ter mais de uma solução.

## Conclusão

Estes scripts são exemplos práticos de como a biblioteca `sympy` do Python pode ser utilizada para resolver equações matemáticas de forma eficiente. Eles são adequados para fins educacionais, especialmente para estudantes que estão aprendendo sobre equações lineares e quadráticas.
