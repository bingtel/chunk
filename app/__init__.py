#-*-coding: utf-8-*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/files', methods=['POST'])
def upload_file():
    f = request.files['file']
    chunk_num = request.values.get('resumableChunkNumber')
    f.save(f.filename+str(chunk_num))
    return 'success'
