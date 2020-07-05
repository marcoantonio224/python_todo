# This is a One-to-Many Relationship of models with TodoList & Todo items

# Parent Model for Todo item
def modelTodoListHandler(db):
  class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # Initialize a relationship with child model
    todos = db.relationship('Todo', backref='list', lazy=True, cascade="all, delete, delete-orphan")
  return TodoList

# Child Model for TodoList
def modelTodoHandler(db):
  class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    # Initialize a Foregin Key for link to the parent model
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
      return f'<Todo {self.id} {self.description}>'
  # Return the Todo class
  return Todo
