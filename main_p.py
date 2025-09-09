from flask import Flask
from deep_translator import GoogleTranslator
from textblob import TextBlob

app = Flask('__name__')

@app.route('/')
def home():
    return "Minha primeira API."


@app.route('/sentimento/<frase>')
def sentimento(frase):
    frase = GoogleTranslator(source='pt', target='en').translate(frase)
    tb_en = TextBlob(frase)
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(debug=True)