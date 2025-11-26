from flask import Flask, request
from flask_cors import CORS
import src.config.db
import mysql.connector


app = Flask(__name__)
CORS(app) 



# Correr la apliación en debug
if __name__ == '__main__':
    app.run(debug=True)