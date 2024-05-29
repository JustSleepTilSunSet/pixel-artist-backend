from flask import Flask, jsonify,request
from model.Constants import status
def home():
    return jsonify({'message': 'hola'})

def saveImage():
    print("Received data:", request.json)
    return jsonify({'status': status["SUCCESS"], 'message': 'Hello, world!'})