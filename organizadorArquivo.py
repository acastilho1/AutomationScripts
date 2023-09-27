import os
from tkinter.filedialog import askdirectory

path = askdirectory(title= "Selecione uma pasta")

lista_arquivos = os.listdir(path)

locais = {
    "imagens" : {" .png", ".jpg"},
    "planilhas":{".xlsx", ".csv"},
    "pdfs": {".pdf"},
    "musica":{".mp4", ".mp5"}   
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{path}/{arquivo}")

    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{path}/{pasta}"):
                os.mkdir(f"{path}/{pasta}")
            os.rename(f"{path}/{arquivo}", f"{path}/{pasta}/{arquivo}")