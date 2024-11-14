from flask import Flask, jsonify,request
from model.Constants import status
import base64
from model.clients.sftpClient import uploadFile;
from flask_jwt_extended import decode_token
from model.database.initdb import connectInitDatabase,createSession;
from model.database.repository.PaintingRepository import Painting

import json
# NOTICE: 預檢類型?前端上傳畫作的類型是否唯一？
def saveImage():
    data = request.files['painting'];
    userToken = request.headers.get('Authorization');
    token = userToken.split('Bearer')[1].strip();
    account = None
    try:
        # Check the header exist token.
        connectInitDatabase();
        session = createSession();

        userInfo = decode_token(token);
        account = json.loads(userInfo["sub"])["account"]; # json string to json.
        # FileStorage一但使用完save或read,cache就會清空，所以這兩行只能二擇一
        # data.save('hi.jpeg'); #FileStorge 可以直接打save
        file_bytes = data.read();
        # print(file_bytes);
        uploadFile(file_bytes,'./share/testing.jpeg');
        session.add(Painting(account = account,paintingName = "testing.jpeg"));
        session.commit();
        
    except Exception as e:
        print(str(e));
        return jsonify({'status': status["LOGIN_FAIL"]})

    return jsonify({'status': status["SUCCESS"]})