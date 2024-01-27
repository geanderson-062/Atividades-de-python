# Definição da função que calcula o IMC
def calcular_imc(peso, altura):
    # Cálculo do IMC: peso dividido pelo quadrado da altura
    imc = peso / (altura**2)
    # Retorna o valor calculado do IMC
    return imc


# Dados de exemplo
peso = 70  # Peso em quilogramas
altura = 1.75  # Altura em metros

# Chamada da função para calcular o IMC com os dados fornecidos
imc = calcular_imc(peso, altura)

# Exibição do resultado, arredondando o IMC para duas casas decimais
print("Seu IMC é:", round(imc, 2))
