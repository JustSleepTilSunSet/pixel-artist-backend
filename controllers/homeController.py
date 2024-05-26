from flask import Flask, jsonify,request

def home():
    return jsonify({'message': 'hola'})

def saveImage():
    print("Received data:", request.json)
    return jsonify({'message': 'Hello, world!'}), 200