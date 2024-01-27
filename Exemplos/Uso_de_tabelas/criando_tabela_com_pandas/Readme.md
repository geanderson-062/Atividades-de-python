# README: Criação e Visualização de Tabela de Dados com Pandas

Este documento oferece uma visão geral e instruções de uso para um script Python que cria e imprime uma tabela de dados utilizando a biblioteca Pandas. O script é ideal para iniciantes que desejam aprender como manipular dados tabulares em Python.

## Descrição

O script demonstra como criar uma tabela de dados simples usando o Pandas, uma poderosa biblioteca de manipulação e análise de dados em Python. Este exemplo pode ser usado como ponto de partida para projetos de análise de dados, onde é necessário criar, manipular e visualizar dados tabulares.

## Pré-requisitos

Para executar este script, é necessário ter Python instalado em seu sistema, além da biblioteca Pandas. Caso não tenha o Pandas instalado, ele pode ser facilmente adicionado utilizando o gerenciador de pacotes pip com o comando `pip install pandas`.

## Estrutura do Código

O código é estruturado da seguinte forma:

- Importação da biblioteca Pandas.
- Criação de um dicionário `dados` contendo listas de informações.
- Conversão do dicionário `dados` em um DataFrame do Pandas chamado `tabela`.
- Impressão da tabela.

## Código

```python
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
```

## Executando o Script

1. Salve o código em um arquivo `.py`.
2. Execute o arquivo usando um interpretador Python.
3. A tabela será impressa no console ou terminal.

## Conclusão

Este script é um exemplo básico de como utilizar o Pandas para criar e visualizar dados tabulares em Python. É uma introdução útil à manipulação de dados para análises mais complexas e pode ser ampliado para incluir funcionalidades como leitura de dados de arquivos, manipulação de colunas e linhas, e realização de cálculos estatísticos.
