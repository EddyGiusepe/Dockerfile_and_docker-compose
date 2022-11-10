'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    '''Função de teste apenas'''
    return "Olá, estou na aplicação setada!"
