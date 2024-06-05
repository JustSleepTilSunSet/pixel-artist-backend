from flask import Flask,request
from flask_cors import CORS
from controllers.homeController import home, saveImage
import model.clients.gcsClient;

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080"])
app.add_url_rule('/home', 'home', home, methods=['GET'])
app.add_url_rule('/saveImage', 'saveImage', saveImage, methods=['POST'])

@app.route("/")
def hello_world():
    return "hola"

if __name__ == '__main__':
    app.run(port=10000)
    # app.run(debug=True)// To cancel debug mode for external to connect the service.