from docx import Document
from datetime import datetime

arquivo = "Oficio modelo.docx"
documento = Document(arquivo)
contador = 1

while True:
    contador += 1

    nome = "Rickson Henrique Alves da Costa" # Ou puxar de algum lugar
    dado1 = "Estágiario"
    dado2 = "HNL"
    dia = str(datetime.now().day)
    mês = str(datetime.now().month)
    ano = str(datetime.now().year)

    referencias = {
        "Nome da Pessoa" : nome,
        "Cargo" : dado1,
        "Órgão" : dado2,
        "05" : dia,
        "dezembro" : mês,
        "2023" : ano,   
        "------" : contador,
        'Descrever, de forma sucinta, o conteúdo do documento___' : "MENSAGEM DO COMENTO",
        }

    for paragrafo in documento.paragraphs:
        for codigo in referencias:
            valor = referencias[codigo]
            paragrafo.text = paragrafo.text.replace(codigo, str(valor))
    documento.save(f"Documento de {nome} - N° {contador}.docx")

    break