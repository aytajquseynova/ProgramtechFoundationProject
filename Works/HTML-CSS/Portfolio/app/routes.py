#app/routes

from flask import render_template,redirect,url_for,request
from admin.routes import feedback, portfolio, education, experience
from run import app

@app.route("/")
def index():
    from models import Experience
    from models import Education
    from models import Feedbacks
    from models import Portfolio
    experience=Experience.query.all()
    education=Education.query.all()
    feedbacks = Feedbacks.query.all()
    portfolios = Portfolio.query.all()
    return render_template("app/index.html",feedbacks=feedbacks, portfolios=portfolios, education=education, experience=experience)