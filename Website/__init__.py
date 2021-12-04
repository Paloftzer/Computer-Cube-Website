from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Website.db"
app.config["SECRET_KEY"] = "123456789123456789123456"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Website import routes