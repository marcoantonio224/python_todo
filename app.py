from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routesHandler
from model import modelHandler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/todoapp'
db = SQLAlchemy(app)

# Create an instance of a Todo model
todo = modelHandler(db)
# Pass the app, render_template, and model to route handler
routesHandler(app, todo, db)
