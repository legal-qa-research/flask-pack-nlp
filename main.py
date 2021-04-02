from flask import Flask, request
from module import correct, gen_sequence

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/spell-correction', methods=['POST'])
def spell_correction():
    sentence = request.get_json().get('sentence')

    return {
        'correctSent': correct(sentence)
    }


@app.route('/dia-res', methods=['POST'])
def diacritic_restoration():
    sentence = request.get_json().get('sentence')

    return {
        'correctSent': gen_sequence(sentence)
    }
