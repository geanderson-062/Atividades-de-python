import tkinter as tk
from tkinter import filedialog
import openpyxl


def salvar_excel():
    # Coletando os dados
    dados = {
        "ID": id_entry.get(),
        "Cliente": cliente_entry.get(),
        "Produto": produto_entry.get(),
        "Data": data_entry.get(),
    }

    # Criando o workbook e adicionando os dados
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(list(dados.keys()))  # Cabeçalhos
    sheet.append(list(dados.values()))  # Valores

    # Pedindo ao usuário para escolher onde salvar o arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if file_path:
        workbook.save(file_path)


# Configuração da janela Tkinter
root = tk.Tk()
root.title("Gerador de Planilha Excel")

# Campos de entrada
tk.Label(root, text="ID").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Cliente").grid(row=1, column=0)
cliente_entry = tk.Entry(root)
cliente_entry.grid(row=1, column=1)

tk.Label(root, text="Produto").grid(row=2, column=0)
produto_entry = tk.Entry(root)
produto_entry.grid(row=2, column=1)

tk.Label(root, text="Data").grid(row=3, column=0)
data_entry = tk.Entry(root)
data_entry.grid(row=3, column=1)

# Botão para salvar os dados em Excel
save_button = tk.Button(root, text="Salvar como Excel", command=salvar_excel)
save_button.grid(row=4, column=0, columnspan=2)

# Executa a aplicação
root.mainloop()
