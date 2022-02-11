#app/routes

from flask import render_template,redirect,url_for,request
from admin.routes import feedback, portfolio, education
from run import app

@app.route("/")
def index():
    from models import Education
    from models import Feedbacks
    from models import Portfolio
    # about = About.query.all()
    education=Education.query.all()
    feedbacks = Feedbacks.query.all()
    portfolios = Portfolio.query.all()
    return render_template("app/index.html",feedbacks=feedbacks, portfolios=portfolios, education=education)