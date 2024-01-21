import openpyxl

# Cria um novo workbook (arquivo Excel)
workbook = openpyxl.Workbook()

# Seleciona a planilha ativa
sheet = workbook.active

# Define o título da planilha
sheet.title = "Exemplo de Planilha"

# Adicionando cabeçalhos
headers = ["ID", "Nome", "Profissão"]
sheet.append(headers)

# Adicionando algumas linhas de dados
dados = [
    [1, "João Silva", "Engenheiro"],
    [2, "Maria Oliveira", "Médica"],
    [3, "Carlos Souza", "Professor"],
]

for row in dados:
    sheet.append(row)

# Salva o arquivo Excel
workbook.save("ExemploPlanilha.xlsx")
