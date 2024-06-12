from flask import Flask, jsonify,request
from model.Constants import status
import base64
from model.clients.sftpClient import uploadFile;
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