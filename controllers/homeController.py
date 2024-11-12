from flask import Flask, jsonify,request
from model.Constants import status
import base64
from model.clients.sftpClient import uploadFile;

def home():
    return jsonify({'message': 'hola'})