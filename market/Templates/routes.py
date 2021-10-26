from flask.helpers import flash
from market import app
from flask import render_template, redirect, url_for
from market import db
from market.models import Item, User
from market.forms import RegisterForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tjanster")
def tjanster_page():
    return render_template("tjänster.html")

@app.route("/omoss")
def Om_oss_page():
    return render_template("omoss.html")

@app.route("/kontakt")
def kontakt_page():
    return render_template("kontakt.html")

@app.route("/login")
def login_page():
    return render_template("login.html")