# README: Exibição de Mensagem de Erro com Tkinter em Python

Este documento fornece uma explicação sobre um script Python simples que utiliza a biblioteca Tkinter para criar uma interface gráfica do usuário (GUI) com um botão. Quando o botão é pressionado, uma caixa de diálogo de mensagem de erro é exibida.

## Descrição

O script cria uma janela de aplicativo GUI básica com um único botão. Ao clicar nesse botão, uma caixa de mensagem de erro é exibida na tela. Este exemplo é útil para entender como eventos de interface gráfica são manipulados em Python e como as caixas de diálogo podem ser usadas para exibir informações aos usuários.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. A biblioteca Tkinter geralmente vem pré-instalada com o Python. Não há necessidade de instalar pacotes adicionais.

## Estrutura do Código

O script segue esta estrutura básica:

- Importação das bibliotecas necessárias (`tkinter` e `messagebox` de `tkinter`).
- Definição de uma função `exibir_mensagem_de_erro` que exibe uma caixa de diálogo de erro quando chamada.
- Criação de uma janela principal (`janela`) usando Tkinter.
- Adição de um botão (`botao`) que, quando pressionado, chama a função `exibir_mensagem_de_erro`.

## Código

```python
import tkinter as tk
from tkinter import messagebox

def exibir_mensagem_de_erro():
    messagebox.showerror("Erro", "Ocorreu um erro. Por favor, tente novamente.")

# Criação da janela
janela = tk.Tk()

# Botão que exibe a mensagem de erro
botao = tk.Button(janela, text="Exibir Erro", command=exibir_mensagem_de_erro)
botao.pack()

# Execução da janela
janela.mainloop()
```

## Executando o Script

1. Salve o script em um arquivo com a extensão `.py`.
2. Execute o arquivo em um ambiente que suporte a execução de scripts Python.
3. Uma janela GUI com um botão será exibida.
4. Ao clicar no botão "Exibir Erro", uma caixa de mensagem de erro será mostrada.

## Conclusão

Este script é uma introdução prática ao uso de caixas de diálogo em aplicações GUI com Python e Tkinter. Ele demonstra como criar uma janela simples, adicionar elementos interativos e manipular eventos, como cliques de botão, para exibir mensagens ao usuário. Este exemplo pode ser particularmente útil para iniciantes em programação Python e desenvolvimento de interfaces gráficas.
