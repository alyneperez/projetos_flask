from flask import render_template, flash, redirect, url_for
from flask_login import login_manager, login_user
from flask.helpers import flash, url_for
from flask_login.utils import logout_user
from flask_wtf import form
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login" , methods=["GET" , "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in.")
        else:
            flash("Invalid Login.")
    return render_template('login.html' ,
                            form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
