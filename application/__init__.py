"""
Flask Application: This module defines a simple Flask web application.
"""


from flask_pymongo import PyMongo
from flask import Flask
# from application import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = '395633a8b3997cf522a2db01a9428092b649273d'
app.config['MONGO_URI'] = "mongodb://localhost:27017/Flask"

# set mongo db
client = PyMongo(app)
db = client.db
