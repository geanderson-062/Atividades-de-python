from sympy import symbols, Eq, solve

# Definir o símbolo
x = symbols('x')

# Definir a equação
equacao = Eq(x**2 + 6*x , 2*x - 3) 

# resolver a equação 
solucao = solve(equacao, x) 

print(solucao) 

 # O resultado será [-3, -1]