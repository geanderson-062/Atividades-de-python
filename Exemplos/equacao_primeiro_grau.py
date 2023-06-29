from sympy import symbols, Eq, solve

# Definir o símbolo
x = symbols('x')

# Definir a equação
equacao = Eq(2*x + 4, 10)

# Resolver a equação
solucao = solve(equacao, x)

print(solucao) 

 # O resultado será [3]
