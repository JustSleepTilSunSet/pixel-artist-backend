from flask import Flask, jsonify

def home():
    return jsonify({'message': 'hola'})
