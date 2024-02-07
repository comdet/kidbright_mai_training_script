from flask import *
from fileinput import filename
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping():
    # return json 
    return jsonify({'response': 'pong'})

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return jsonify({'response': 'success'})

@app.route('/train', methods=['POST'])
def train():
    if request.method == 'POST':
        data = request.json
        return jsonify({'response': 'success', 'data': data})
    elif request.method == 'GET':
        return jsonify({'response': 'success'})