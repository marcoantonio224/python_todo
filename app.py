from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routesHandler
from models import modelTodoHandler, modelTodoListHandler
from flask_migrate import Migrate
from flask_debug import Debug


app = Flask(__name__)
Debug(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/todoapp'
# To update the changes in static files and prevent caching in browsers
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)


# Create migrations throughout application
migrate = Migrate(app, db)
# Create an instance of a TodoList model
list = modelTodoListHandler(db)
# Create an instance of a Todo model
todo = modelTodoHandler(db)
# Pass the app, render_template, and model to route handler and initate routes
routesHandler(app, todo, list, db)

#Run app
if __name__ == '__main__':
  app.run(debug=True)
