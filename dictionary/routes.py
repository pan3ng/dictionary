from flask import render_template, url_for
from dictionary import app

# from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('dictionary.html')