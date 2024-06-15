from flask import Flask,request
from flask_cors import CORS
from controllers.homeController import home, saveImage, login
import model.clients.gcsClient;
from model.clients.sftpClient import sftpConnect,getDir;

sftpConnect()
getDir()
app = Flask(__name__)
CORS(app, origins=["http://localhost:8081"])
app.add_url_rule('/home', 'home', home, methods=['GET'])
app.add_url_rule('/saveImage', 'saveImage', saveImage, methods=['POST'])
app.add_url_rule('/login', 'login', login, methods=['POST'])

@app.route("/")
def hello_world():
    return "hola"

if __name__ == '__main__':
    app.run(port=10000)
    # app.run(debug=True)// To cancel debug mode for external to connect the service.