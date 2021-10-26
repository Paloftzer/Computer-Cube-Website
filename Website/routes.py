from flask.helpers import flash
from Website import app
from flask import render_template, redirect, url_for
from Website import db
from Website.models import User
from Website.forms import RegisterForm

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

@app.route("/login", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username = form.username.data,
            email_address = form.email_address.data,
            password = form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("home"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error creating user: {err_msg}", category="danger")
    return render_template("login.html", form=form)