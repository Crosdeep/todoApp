#routes
from crypt import methods

from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Todo

#blueprint olusturma
todo_db = Blueprint('todo',__name__)

#Anasayfa
@todo_db.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


#Görev olusturma
@todo_db.route("/create", methods=['POST','GET'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        task = request.form['task']
        description = request.form.get('description')

        new_task = Todo(title=title, task=task, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('todo.index'))

#Görev detay sayfası
@todo_db.route('/task/<int:id>')
def detail_task(id):
    task = Todo.query.get_or_404(id)
    return  render_template('task_detail.html', task=task)