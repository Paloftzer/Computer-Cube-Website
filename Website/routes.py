from flask.helpers import flash
from flask_login import current_user, login_user, logout_user
from flask_mail import Message
from Website import app
from flask import render_template, redirect, url_for
from Website import db
from Website.models import User
from Website.forms import RegisterForm, LoginForm, SupportForm
from Website import mail

@app.route("/")
def home():
    return render_template("main/index.html")

@app.route("/tjanster")
def tjanster_page():
    return render_template("main/tjänster.html")

@app.route("/omoss")
def Om_oss_page():
    return render_template("main/omoss.html")

@app.route("/kontakt", methods=["GET", "POST"])
def kontakt_page():
    supportform = SupportForm()
    if supportform.validate_on_submit():
        msg = Message(str(supportform.email_address.data), recipients = ["computercubeuf@gmail.com"])
        msgbody = str(supportform.name.data) +"\n"+ str(supportform.subject.data)
        msg.body = msgbody
        mail.send(msg)
        flash("Successfully sent message! Please wait for our response!", category="alert")
        return redirect(url_for("kontakt_page"))
    return render_template("main/kontakt.html", supportform=supportform)

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
    if current_user.is_authenticated:
        flash("You cannot log in while logged in!", category="danger")
        return redirect(url_for("home"))
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Successfully logged in as {attempted_user.username}", category="success")
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password, please try again!", category="danger")
    return render_template("main/login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Logout successful!", category="info")
    return redirect(url_for("home"))

@app.route("/account")
def account_page():
    return render_template("main/account.html")