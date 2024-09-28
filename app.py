#app
from logging import DEBUG

from flask import Flask
from config import Config
from models import db
from routes import todo_db

app = Flask(__name__)
app.config.from_object(Config)

#veritabanı başlat
db.init_app(app)

#Blueprint kaydet
app.register_blueprint(todo_db)

#Veritabnı tablo olusturma
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

