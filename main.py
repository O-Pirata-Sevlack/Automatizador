from docx import Document
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')


arquivo = "Oficio modelo.docx"
documento = Document(arquivo)
contador = 1

while True:
    contador += 1

    Genero_R = "O Senhor"
    Nome_R = "Emmanuel Rhadma" # Ou puxar de algum lugar
    Cargo_R = "Cooordenador"
    Órgão_R = "HNL"
    Endereço_R = "Av. Cap. José Pessoa, 1140, Jaguaribe"
    CEP_R = "58015-170"
    Cidade_R = "João Pessoa/PB"
    Assunto = "Projeto de automatização de documentos"
    dia = str(datetime.now().day)
    mês = datetime.now()
    mês = mês.strftime('%B')
    ano = str(datetime.now().year)

    referencias = {
        "Genero_R" : Genero_R,
        "Nome_R" : Nome_R,
        "Cargo_R" : Cargo_R,
        "Órgão_R" : Órgão_R,
        "Endereço_R" : Endereço_R,
        "CEP_R" : CEP_R,   
        "Cidade_R" : Cidade_R,
        "dia" : dia,
        "mês" : mês,
        "ano" : ano,
        "número" : contador,

        "Descrever, de forma sucinta, o conteúdo do documento" : Assunto,
        }

    for paragrafo in documento.paragraphs:
        for codigo in referencias:
            valor = referencias[codigo]
            paragrafo.text = paragrafo.text.replace(codigo, str(valor))
    documento.save(f"Documento de {Nome_R} - N° {contador}.docx")

    break