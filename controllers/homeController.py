from flask import Flask, jsonify,request
from model.Constants import status
import base64
from model.clients.sftpClient import uploadFile;
from dotenv import dotenv_values
import os
from model.Secret import Secret;

def home():
    return jsonify({'message': 'hola'})

def saveImage():
    resp = request.json
    fave_website_split = resp['image'].split(",")
    try:
        file_content=base64.b64decode(fave_website_split[1])
        with open("q1.jpeg","wb") as f:
            f.write(file_content)
        uploadFile(file_content,'./share/testing.jpeg')
    except Exception as e:
        print(str(e))

    return jsonify({'status': status["SUCCESS"], 'message': 'Hello, world!'})

def login():
    resp = request.json
    try:
        print(jsonify(resp))
        isVaild = resp["account"] == os.getenv("TESTING_USER_ACCOUNT") and resp["pwd"] == os.getenv("TESTING_USER_PWD")
        if isVaild !=True:
            return jsonify({'status': status["FAIL"], 'message': 'login failed.'})
        
        print(isVaild);
        return jsonify({'status': status["SUCCESS"], 'message': 'login success'})
    except Exception as e:
        print(str(e))

    return jsonify({'status': status["SUCCESS"], 'message': 'Hello, world!'})

def loginByGuest():
    try:
        secret = Secret()
        return jsonify({'account': secret.generateRandString(16), 'password': secret.generateRandString(8)})
    except Exception as e:
        print(str(e))
        return jsonify({'message':"Server error"});
