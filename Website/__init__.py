from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from Website.gen_key import key

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Website.db"
app.config["SECRET_KEY"] = key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  
login_manager = LoginManager(app)

from Website import routes