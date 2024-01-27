# Definição da classe Pessoa
class Pessoa:
    # Método construtor para inicializar cada instância da classe
    def __init__(self, peso, altura):
        self.peso = peso  # Atribuição do peso ao atributo da classe
        self.altura = altura  # Atribuição da altura ao atributo da classe

    # Método para calcular o IMC da instância
    def calcular_imc(self):
        # Cálculo do IMC usando os atributos da instância
        return self.peso / (self.altura**2)


# Criação de uma instância da classe Pessoa com dados de exemplo
pessoa = Pessoa(70, 1.75)  # 70 kg, 1.75 metros

# Chamada do método para calcular o IMC da instância criada
imc = pessoa.calcular_imc()

# Exibição do IMC, arredondando para duas casas decimais
print("Seu IMC é:", round(imc, 2))
