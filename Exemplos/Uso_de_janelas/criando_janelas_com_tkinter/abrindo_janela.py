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
