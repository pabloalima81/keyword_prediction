import pandas as pd
from flask import Flask, jsonify
from utils.main import *


app = Flask(__name__)

@app.route('/')
def index():
    return 'keyword Prediction'

@app.route("/keyword/<string:word>")
def keyword(word):
    word_prediction = str(keyword_prediction(word))
    return (jsonify(word_prediction))

app.run(debug=True)