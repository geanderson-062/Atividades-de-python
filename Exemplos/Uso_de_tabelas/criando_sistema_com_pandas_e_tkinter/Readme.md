# README: Exibição de Tabela de Dados com Pandas e Tkinter em Python

Este documento fornece detalhes e instruções de uso para um script Python que combina a biblioteca Pandas para manipulação de dados e Tkinter para interface gráfica do usuário (GUI). O script cria e exibe uma tabela de dados em uma janela GUI.

## Descrição

O script demonstra como criar uma tabela de dados simples usando Pandas e depois exibi-la em uma janela GUI usando Tkinter. Este exemplo é particularmente útil para visualizar dados tabulares em uma aplicação Python e pode ser adaptado para projetos que requerem a exibição de dados em formato de tabela numa interface gráfica.

## Pré-requisitos

Para executar este script, você precisará ter Python instalado em seu sistema, juntamente com as bibliotecas Pandas e Tkinter. Tkinter geralmente vem pré-instalado com o Python, mas Pandas pode precisar ser instalada separadamente usando um gerenciador de pacotes como pip.

## Estrutura do Código

O código segue esta estrutura básica:

- Importação das bibliotecas Pandas e Tkinter.
- Criação de um conjunto de dados (`dados`) e conversão desses dados em um DataFrame do Pandas (`tabela`).
- Definição da função `exibir_tabela` que cria uma janela GUI e exibe a tabela de dados nessa janela.
- Chamada da função `exibir_tabela` para executar o programa.

## Código

```python
import pandas as pd
import tkinter as tk

# Criar os dados
dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
}

# Criar o DataFrame (tabela)
tabela = pd.DataFrame(dados)

# Função para exibir a tabela na janela
def exibir_tabela():
    root = tk.Tk()
    root.title("Exemplo de Tabela")

    # Centralizar a janela
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Estilizar a tabela
    tabela_fonte = ("Helvetica", 12)
    tabela_cabecalho_fonte = ("Helvetica", 14, "bold")

    # Criar a tabela
    tabela_texto = tk.Text(root, font=tabela_fonte)
    tabela_texto.insert(tk.END, tabela.to_string(index=False))
    tabela_texto.pack(pady=10)

    # Configurar a rolagem da tabela
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabela_texto.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tabela_texto.yview)

    # Iniciar o loop de eventos da janela
    root.mainloop()

# Chamar a função para exibir a tabela na janela
exibir_tabela()
```

## Executando o Script

1. Salve o código em um arquivo `.py`.
2. Garanta que o Pandas esteja instalado em seu ambiente Python.
3. Execute o arquivo em um ambiente Python.
4. Uma janela GUI será aberta, mostrando os dados tabulares.

## Conclusão

Este script é um exemplo prático da integração entre Pandas para manipulação de dados e Tkinter para criação de interfaces gráficas. É uma boa base para aplicativos que precisam visualizar dados de forma simples e eficaz em uma interface gráfica.
