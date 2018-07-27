# from flask_restplus import *
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HTML does not work'



