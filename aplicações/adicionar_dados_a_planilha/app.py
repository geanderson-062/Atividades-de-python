import tkinter as tk
import customtkinter
from tkinter import filedialog
import openpyxl

# Configuração da janela Tkinter usando customtkinter
root = customtkinter.CTk()
root.title("Gerador de Planilha Excel")

# Definindo tamanho e outras propriedades da janela
root.geometry("700x400")
root.title("Sistema de Planilhas")
# Certifique-se de que o ícone 'icone.ico' está no diretório do script
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


# Campos de entrada com customtkinter
customtkinter.CTkLabel(root, text="ID").grid(row=0, column=0)
id_entry = customtkinter.CTkEntry(root)
id_entry.grid(row=0, column=1)

customtkinter.CTkLabel(root, text="Cliente").grid(row=1, column=0)
cliente_entry = customtkinter.CTkEntry(root)
cliente_entry.grid(row=1, column=1)

customtkinter.CTkLabel(root, text="Produto").grid(row=2, column=0)
produto_entry = customtkinter.CTkEntry(root)
produto_entry.grid(row=2, column=1)

customtkinter.CTkLabel(root, text="Data").grid(row=3, column=0)
data_entry = customtkinter.CTkEntry(root)
data_entry.grid(row=3, column=1)

# Botão para salvar os dados em Excel
save_button = customtkinter.CTkButton(
    root, text="Salvar como Excel", command=salvar_excel
)
save_button.grid(row=4, column=0, columnspan=2)

# Executa a aplicação
root.mainloop()
