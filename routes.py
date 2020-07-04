from flask import render_template, request, redirect, url_for, jsonify, abort
import sys

# Handle errors in api requests
def handleError():
    db.session.rollback()
    print(sys.exc_info())

def routesHandler(app, Todo, TodoList, db):
  # Render Home page
  @app.route('/')
  def index():
    return redirect(url_for('get_list_todos', list_id = 1))

  #Create a list
  @app.route('/lists/create', methods=['POST'])
  def create_list():
    print('CREATING A s', request.get_json())
    error = False
    body = {}
    try:
      name = request.get_json()['data']['name']
      list = TodoList(name = name)
      db.session.add(list)
      db.session.commit()
      body['list'] = name
    except:
      error = True
      handleError()
    finally:
      db.session.close()
    if error:
      abort(400)
    else:
      return jsonify(body)


  # Render a particular List
  @app.route('/lists/<list_id>')
  def get_list_todos(list_id):
    return render_template('index.html', lists=TodoList.query.all(),
        active_list=TodoList.query.get(list_id),
        todos = Todo.query.filter_by(list_id=list_id).order_by('id').all())

  # Create a todo item
  @app.route('/todos/create', methods=['POST'])
  def create():
    error = False
    body = {}
    try:
      description = request.get_json()['data']['description']
      list_id = request.get_json()['data']['list_id']
      todo = Todo(description = description, list_id = int(list_id))
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
