from docx import Document
from flask import Flask, render_template, request
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

arquivo = "Oficio modelo.docx"
documento = Document(arquivo)
contador = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Genero_R = request.form['P1']
        Nome_R = request.form['P1']
        Cargo_R = request.form['P1']
        Órgão_R = request.form['P1']
        Endereço_R = request.form['P1']
        CEP_R = request.form['P1']
        Cidade_R = request.form['P1']
        Assunto = request.form['P1']
        Nome_E = request.form['P1']
        Genero_E = request.form['P1']
        Cargo_E = request.form['P1']
        Texto = request.form['P1']
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
        "Nome_E" : Nome_E,
        "Gênero_E" : Genero_E,
        "Cargo_E" : Cargo_E,
        "Corpo do documento com identificação de primeira linha" : Texto,

        }

    for paragrafo in documento.paragraphs:
        for codigo in referencias:
            valor = referencias[codigo]
            paragrafo.text = paragrafo.text.replace(codigo, str(valor))
    documento.save(f"Documento de {Nome_E} - N° {contador}.docx")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)