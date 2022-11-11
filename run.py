'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
from src import UserRepo
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    '''Função de teste apenas'''
    return "Olá, estou na aplicação setada!"

@app.route("/insert", methods=["POST"])
def insert():
    '''Função de insert'''
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"])

    return 'ok'

