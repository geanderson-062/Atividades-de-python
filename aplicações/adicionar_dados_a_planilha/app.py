import tkinter as tk
import customtkinter
from tkinter import filedialog
import openpyxl

# Configuração da janela Tkinter usando customtkinter
root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Sistema de Planilhas")
root.resizable(False, False)

# Definindo o tema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


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


# Ajustes de centralização para o grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)

# Título "Cadastrar"
titulo_label = customtkinter.CTkLabel(root, text="Cadastrar", font=("Roboto", 25))
titulo_label.grid(row=1, column=1, columnspan=2, pady=(10, 20))

# Campos de entrada com customtkinter
id_entry = customtkinter.CTkEntry(root, placeholder_text="ID")
id_entry.grid(row=2, column=1, columnspan=2, pady=5)

cliente_entry = customtkinter.CTkEntry(root, placeholder_text="Cliente")
cliente_entry.grid(row=3, column=1, columnspan=2, pady=5)

produto_entry = customtkinter.CTkEntry(root, placeholder_text="Produto")
produto_entry.grid(row=4, column=1, columnspan=2, pady=5)

data_entry = customtkinter.CTkEntry(root, placeholder_text="Data")
data_entry.grid(row=5, column=1, columnspan=2, pady=5)

# Botão para salvar os dados em Excel
save_button = customtkinter.CTkButton(
    root, text="Salvar como Excel", command=salvar_excel
)
save_button.grid(row=6, column=1, columnspan=2, pady=5)

# Executa a aplicação
root.mainloop()
