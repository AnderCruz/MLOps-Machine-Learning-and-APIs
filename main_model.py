from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from deep_translator import GoogleTranslator
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

colunas = ['tamanho','ano','garagem']
modelo = pickle.load(open('modelo.sav','rb'))

app = Flask('__name__')
app.config['BASIC_AUTH_USERNAME'] = 'anderjcruz'
app.config['BASIC_AUTH_PASSWORD'] = 'Nmaster'
basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def home():
    return "Minha primeira API."

@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    frase = GoogleTranslator(source='pt', target='en').translate(frase)
    tb_en = TextBlob(frase)
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True)