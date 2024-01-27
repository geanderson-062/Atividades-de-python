# README: Abertura de Nova Janela com Tkinter em Python

Este documento oferece uma visão geral e instruções de uso para um script Python que cria uma interface gráfica do usuário (GUI) com a biblioteca Tkinter. O script principal abre uma nova janela ao clicar em um botão.

## Descrição

O objetivo do script é demonstrar a criação de múltiplas janelas em uma aplicação GUI usando Tkinter, uma biblioteca padrão do Python para interfaces gráficas. O script cria uma janela principal com um botão. Quando esse botão é pressionado, uma nova janela (secundária) é aberta.

## Pré-requisitos

Para executar este script, você precisa ter o Python instalado em seu sistema. Tkinter geralmente vem pré-instalado com o Python, portanto, não são necessárias instalações adicionais.

## Estrutura do Código

O código é estruturado da seguinte maneira:

- Importação do módulo Tkinter.
- Definição da função `abrir_janela()`, responsável por abrir uma nova janela quando chamada.
- Criação da janela principal (`root`).
- Adição de um botão (`botao`) na janela principal, que chama a função `abrir_janela` quando pressionado.
- Execução do loop principal da aplicação.

## Código

```python
import tkinter as tk

def abrir_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.geometry("300x200")
    nova_janela.title("Nova Janela")

    label = tk.Label(nova_janela, text="Nova janela aberta!")
    label.pack(padx=10, pady=10)

root = tk.Tk()

botao = tk.Button(root, text="Abrir Janela", command=abrir_janela)
botao.pack(padx=10, pady=10)

root.mainloop()
```

## Executando o Script

1. Salve o código em um arquivo `.py`.
2. Execute o arquivo em um ambiente que suporte a execução de scripts Python.
3. A janela principal será exibida com um botão rotulado "Abrir Janela".
4. Ao clicar no botão, uma nova janela será aberta com a mensagem "Nova janela aberta!".

## Conclusão

Este script é um exemplo introdutório de como trabalhar com múltiplas janelas em uma aplicação Tkinter. Ele é útil para entender como criar interfaces gráficas interativas e responsivas em Python. Este exemplo pode ser adaptado para aplicações mais complexas que exigem a abertura de várias janelas.
