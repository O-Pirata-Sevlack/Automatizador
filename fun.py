from docx import Document
from datetime import datetime

def editor (arquivo, contador):
    documento = Document(arquivo)
    if editor:
        contador += 1

    nome = "Rickson" # Ou puxar de algum lugar
    dado1 = "Exemplo"
    dado2 = "Exemplo"
    dia = str(datetime.now().day)
    mês = str(datetime.now().month)
    ano = str(datetime.now().year)

    referencias = {
        "VARIAVEL-1" : nome,
        "VARIAVEL-2" : dado1,
        "VARIAVEL-3" : dado2,
        "DIA" : dia,
        "MÊS" : mês,
        "ANO" : ano,   
        "N° Doc" : contador,
        }

    for paragrafo in documento.paragraphs:
        for codigo in referencias:
            valor = referencias[codigo]
            paragrafo.text = paragrafo.text.replace(codigo, valor)
    documento.save(f"Documento de {nome} - N° {contador}.docx")

