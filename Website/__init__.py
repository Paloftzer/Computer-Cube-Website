from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Website.db"
app.config["SECRET_KEY"] = "89057dfe68590bb62ff49eea45fb33812fa05f1930a442b4"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  
login_manager = LoginManager(app)

from Website import routes