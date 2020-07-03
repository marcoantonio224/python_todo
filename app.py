from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routesHandler
from model import modelHandler
from flask_migrate import Migrate
from flask_debug import Debug


app = Flask(__name__)
Debug(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/todoapp'
# To update the changes in static files and prevent caching in browsers
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Create an instance of a Todo model
todo = modelHandler(db)
# Pass the app, render_template, and model to route handler
routesHandler(app, todo, db)

#Run app
if __name__ == '__main__':
  app.run(debug=True)
