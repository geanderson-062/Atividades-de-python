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
