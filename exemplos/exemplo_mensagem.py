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
