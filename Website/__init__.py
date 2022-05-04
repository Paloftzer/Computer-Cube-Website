from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from Website.secrets import emailpass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Website.db"
app.config["SECRET_KEY"] = "89057dfe68590bb62ff49eea45fb33812fa05f1930a442b4"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  
login_manager = LoginManager(app)
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'computercube.help@gmail.com'
app.config['MAIL_PASSWORD'] = emailpass
app.config['MAIL_DEFAULT_SENDER'] = 'computercube.help@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

from Website import routes