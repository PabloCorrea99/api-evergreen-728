from flask import Flask, jsonify, request 
from flask_cors import CORS 
from controllers.Predios import Predio

app = Flask(__name__)
CORS(app)

@app.route('/Predios',methods=['GET'])
def getAll(): 
    return (Predio.list())

@app.route('/Predios',methods=['POST'])
def postOne(): 
    body = request.json 
    return (Predio.create(body))

