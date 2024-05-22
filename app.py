from flask import Flask
from controllers.homeController import home

app = Flask(__name__)
app.add_url_rule('/home', 'home', home, methods=['GET'])

@app.route("/")
def hello_world():
    return "hola"

if __name__ == '__main__':
    app.run(port=10000)
    # app.run(debug=True)// To cancel debug mode for external to connect the service.