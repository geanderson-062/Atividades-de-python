import pandas as pd

# Criar os dados
dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
}

# Criar o DataFrame (tabela)
tabela = pd.DataFrame(dados)

# Imprimir a tabela
print(tabela)
