# README: Aplicação GUI Simples em Python com Tkinter

Este documento oferece uma explicação detalhada sobre um script Python que cria uma interface gráfica do usuário (GUI) simples para capturar dados. Utilizando a biblioteca Tkinter, o script cria uma janela com campos de entrada para o nome e a idade do usuário e um botão para capturar essas informações.

## Descrição

O script usa Tkinter, uma biblioteca padrão do Python para criar interfaces gráficas. O objetivo é criar uma janela com dois campos de entrada onde os usuários podem inserir seu nome e idade. Após o preenchimento dos dados, o usuário pode clicar em um botão para capturar e exibir essas informações no console.

## Pré-requisitos

Certifique-se de que você tem o Python instalado em seu sistema. Tkinter geralmente vem pré-instalado com o Python. Não são necessárias bibliotecas externas adicionais.

## Estrutura do Código

O script é organizado da seguinte forma:

- Importação da biblioteca Tkinter.
- Definição da função `obter_dados()` que captura os dados inseridos e os imprime no console.
- Criação da janela principal (`janela`) usando Tkinter.
- Adição de componentes GUI:
  - `Label` e `Entry` para o nome do usuário.
  - `Label` e `Entry` para a idade do usuário.
  - Um `Button` que, ao ser clicado, chama a função `obter_dados()`.

## Código

```python
import tkinter as tk

def obter_dados():
    nome = campo_nome.get()
    idade = campo_idade.get()

    print("Nome:", nome)
    print("Idade:", idade)

janela = tk.Tk()

# Campo de entrada para o nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
campo_nome = tk.Entry(janela)
campo_nome.pack()

# Campo de entrada para a idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()
campo_idade = tk.Entry(janela)
campo_idade.pack()

# Botão para capturar os dados
botao = tk.Button(janela, text="Capturar Dados", command=obter_dados)
botao.pack()

janela.mainloop()
```

## Executando o Script

1. Salve o script em um arquivo `.py`.
2. Execute o arquivo em um ambiente que suporte a execução de scripts Python.
3. A janela GUI será exibida. Insira o nome e a idade nos campos apropriados.
4. Clique no botão "Capturar Dados" para imprimir as informações no console.

## Conclusão

Este script é um exemplo básico de como criar uma aplicação GUI em Python usando Tkinter. Ele é ideal para iniciantes que desejam aprender como interagir com usuários através de interfaces gráficas e como capturar e manipular dados do usuário em um programa Python.
