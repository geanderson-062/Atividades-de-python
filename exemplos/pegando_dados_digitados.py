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
