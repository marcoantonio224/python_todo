from flask import render_template, request, redirect, url_for, jsonify, abort
import sys

def routesHandler(app, Todo, db):
  @app.route('/')
  def index():
    return render_template('index.html', data = Todo.query.all())

  @app.route('/todos/create', methods=['POST'])
  def create():
    error = False
    body = {}
    try:
      description = request.get_json()['description']
      todo = Todo(description = description)
      db.session.add(todo)
      db.session.commit()
      body['description'] = todo.description
    except:
      error = True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      abort(400)
    else:
      return jsonify(body)
