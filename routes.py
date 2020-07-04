from flask import render_template, request, redirect, url_for, jsonify, abort
import sys
import os

# Handle errors in api requests
def handleError():
    db.session.rollback()
    print(sys.exc_info())

def routesHandler(app, Todo, db):
  # Render Home page
  @app.route('/')
  def index():
    return redirect(url_for('get_list_todos', list_id = 1))

  # Render a particular List
  @app.route('/lists/<list_id>')
  def get_list_todos(list_id):
    return render_template('index.html', data = Todo.query.filter_by(list_id=list_id).order_by('id').all())

  # Create a todo item
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
      handleError()
    finally:
      db.session.close()
    if error:
      abort(400)
    else:
      return jsonify(body)

  # Update the completion of the todo item
  @app.route('/todos/<todo_id>/set-completed', methods=['POST'])
  def set_completed_todo(todo_id):
    try:
      completed = request.get_json()['completed']
      todo = Todo.query.get(todo_id)
      todo.completed = completed
      db.session.commit()
    except:
      handleError()
    finally:
      db.session.close()
    return redirect(url_for('index'))

  # Delete a todo item
  @app.route('/todos/<todo_id>/set-completed', methods=['DELETE'])
  def set_deleted_todo(todo_id):
    try:
      Todo.query.filter_by(id=todo_id).delete()
      db.session.commit()
    except:
      handleError()
    finally:
      db.session.close()
    return jsonify({'sucess': True,'todoID':todo_id})




