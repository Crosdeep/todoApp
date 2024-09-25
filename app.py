from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#postgreSQL veritabanı bağlantısı
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kullanıcı_adı:şifre@localhost/veritabanı_adı'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#görev modeli
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    todo_task = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Veritabanını oluşturmak için
# with app.app_context():
# db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        new_task = Task(title=title, description=description, date=date)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/task/<int:id>')
def task_detail(id):
    task = Task.query.get_or_404(id)
    return render_template('card.html', task=task)

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)