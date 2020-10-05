from os import name
import requests
import json
from flask import Flask, jsonify;

app = Flask(__name__)


r = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
r.headers['content-type']
r.encoding
r.text


@app.route("/")

def home():
       print(r.json())
      
app.run();

