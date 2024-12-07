from flask import Flask,request
from flask_cors import CORS
import os
from controllers.homeController import home
from controllers.PaintingController import saveImage, listImageById, getImageToBase64
from controllers.UserController import login, loginByGuest
from model.clients.sftpClient import sftpConnect,getDir;
from model.database.initdb import connectInitDatabase;
from flask_jwt_extended import JWTManager
sftpConnect()
getDir()
connectInitDatabase()
app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY");
CORS(app, origins=[os.getenv("CORS_DEV_HOST")])
app.add_url_rule('/home', 'home', home, methods=['GET'])
app.add_url_rule('/saveImage', 'saveImage', saveImage, methods=['POST'])
app.add_url_rule('/getImageToBase64', 'getImageToBase64', getImageToBase64, methods=['POST'])
app.add_url_rule('/listImageById', 'listImageById', listImageById, methods=['POST'])
app.add_url_rule('/user/login', 'login', login, methods=['POST'])
app.add_url_rule('/user/loginByGuest', 'loginByGuest', loginByGuest, methods=['POST'])

@app.route("/")
def hello_world():
    return "hola"

if __name__ == '__main__':
    app.run(port=10000)
    # app.run(debug=True)// To cancel debug mode for external to connect the service.