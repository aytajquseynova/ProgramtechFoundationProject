import flask 
from run import app 
from flask import Flask,render_template,url_for,redirect,request
from models import *

@app.route("/admin",methods=["GET","POST"])
def admin(id):
    return render_template("admin/base.html")
#Admin Education
@app.route("/admin/education",methods=["GET","POST"])
def education():
    from models import Education
    import os
    from run import db
    from werkzeug.utils import secure_filename
    education = Education.query.all()
    if request.method=="POST":
        education_date = request.form["time"]
        education_description=request.form["derece"]
        education_title=request.form["tehsilqurumu"]
        education_information=request.form["yer"]
        tehsil = Education(
           education_date=education_date,
           education_description=education_description,
           education_title=education_title,
           education_information=education_information
           )
        db.session.add(tehsil)
        db.session.commit()
        return redirect("/")
    return render_template('admin/tehsil.html',education=education)
#Delete Education
@app.route("/educationDelete/<int:id>",methods=["GET","POST"])
def education_delete(id):
    from models import Education
    import os
    from run import db
    edu =   Education.query.filter_by(id=id).first()
    db.session.delete(education)
    db.session.commit()
    return redirect ("/admin/education")
# Admin Feedbacks
@app.route("/admin/feedbacks",methods=["GET","POST"])
def feedback():
    from models import Feedbacks
    import os
    from run import db
    from werkzeug.utils import secure_filename
    feedbacks = Feedbacks.query.all()
    if request.method=="POST":
        file = request.files['img']
        filename = secure_filename(file.filename)  
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        feedback_rey = request.form["rey"]
        feedback_cmntrname=request.form["cmntrname"]
        feedback_cmntrjob=request.form["cmntrjob"]
        
        prjct = Feedbacks(
            feedback_rey = feedback_rey,
            feedback_img = filename,
            feedback_cmntrname=feedback_cmntrname,
            feedback_cmntrjob=feedback_cmntrjob,
        )
        db.session.add(prjct)
        db.session.commit()
        return redirect("/")
    return render_template('admin/feedbacks.html',feedbacks=feedbacks)

# Delete
@app.route("/feedbackDelete/<int:id>",methods=["GET","POST"])
def feedback_delete(id):
    from models import Feedbacks
    import os
    from run import db
    feedbacks = Feedbacks.query.filter_by(id=id).first()
    db.session.delete(feedbacks)
    db.session.commit()
    return redirect ("/admin/feedbacks")

# Update

@app.route("/feedbackEdit/<int:id>",methods=["GET","POST"])
def feedback_edit(id):
    from models import Feedbacks
    from run import db
    newFeedback = Feedbacks.query.filter_by(id=id).first()
    if request.method=="POST":
        feedbacks = Feedbacks.query.filter_by(id=id).first()
        feedbacks.feedback_rey = request.form["rey"]
        feedbacks.feedback_cmntrname = request.form["cmntrname"]
        feedbacks.feedback_cmntrjob = request.form["cmntrjob"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_feedbacks.html",newFeedback=newFeedback)


@app.route('/admin/portfolio', methods=["GET","POST"])
def portfolio():
    from models import Portfolio
    import os
    from run import db
    from werkzeug.utils import secure_filename
    portfolios = Portfolio.query.all()
    
    if request.method=="POST":
        file = request.files['img']
        filename = secure_filename(file.filename)  
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        portfolio_title = request.form["portfolio_title"]
        prtfl = Portfolio(
            portfolio_title = portfolio_title,
            portfolio_img = filename
        )
        db.session.add(prtfl)
        db.session.commit()
        return redirect("/")
    return render_template('admin/portfolio.html',portfolios=portfolios)


@app.route("/portfolioDelete/<int:id>",methods=["GET","POST"])
def portfolio_delete(id):
    from models import Portfolio
    import os
    from run import db
    portfolios = Portfolio.query.filter_by(id=id).first()

    db.session.delete(portfolios)
    db.session.commit()
    return redirect ("/admin/portfolio")

@app.route('/portfolioEdit/<int:id>',methods=["GET","POST"])
def portfolio_edit(id):
    from models import Portfolio
    from run import db
    newPortfolio = Portfolio.query.filter_by(id=id).first()
    if request.method=="POST":
        portfolios = Portfolio.query.filter_by(id=id).first()
        portfolios.portfolio_title = request.form["portfolio_title"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_portfolio.html",newPortfolio=newPortfolio)