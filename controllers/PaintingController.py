from flask import Flask, jsonify,request
from model.Constants import status
import base64
from model.clients.sftpClient import uploadFile;
# NOTICE: 預檢類型?前端上傳畫作的類型是否唯一？
def saveImage():
    data = request.files['painting'];
    # print(data);
    try:
        # FileStorage一但使用完save或read,cache就會清空，所以這兩行只能二擇一
        # data.save('hi.jpeg'); #FileStorge 可以直接打save
        file_bytes = data.read();
        # print(file_bytes);
        uploadFile(file_bytes,'./share/testing.jpeg');
    except Exception as e:
        print(str(e));

    return jsonify({'status': status["SUCCESS"], 'message': 'Hello, world!'})