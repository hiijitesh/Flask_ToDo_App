from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['SECRET_KEY'] = '395633a8b3997cf522a2db01a9428092b649273d'
app.config['MONGO_URI'] = "mongodb://localhost:27017/Flask"

# set mongo db
client = PyMongo(app)
db = client.db

from application import routes