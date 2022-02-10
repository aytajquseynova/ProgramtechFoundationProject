#app/routes

from flask import render_template,redirect,url_for,request
from admin.routes import feedback
from app import app

@app.route("/")
def portfolio():
    from models import Feedbacks
    feedbacks = Feedbacks.query.all()
    return render_template("app/index.html",feedbacks=feedbacks)