from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug = True)
    
#! This is an alert
#? This is a query
#* Highlighting for important information
#TODO: Learn what TODO means
## Removed comment
# Regular comment