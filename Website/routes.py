from flask.helpers import flash
from flask_login import login_user, logout_user
from Website import app
from flask import render_template, redirect, url_for
from Website import db
from Website.models import User
from Website.forms import RegisterForm, LoginForm

@app.route("/")
def home():
    return render_template("main/index.html")

@app.route("/tjanster")
def tjanster_page():
    return render_template("main/tjänster.html")

@app.route("/omoss")
def Om_oss_page():
    return render_template("main/omoss.html")

@app.route("/kontakt")
def kontakt_page():
    return render_template("main/kontakt.html")

@app.route("/register", methods=["GET", "POST"])
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
    return render_template("main/register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Successfully logged in as {attempted_user.username}", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login failed! Please try again!", category="danger")
    return render_template("main/login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Logout successful!", category="info")
    return redirect(url_for("home"))