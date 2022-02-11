import flask 
from run import app 
from flask import Flask,render_template,url_for,redirect,request
from models import *

@app.route("/admin",methods=["GET","POST"])
def admin():
    return render_template("admin/base.html")
#Admin Experience
@app.route("/admin/experience",methods=["GET","POST"])
def experience():
    from models import Experience
    import os
    from run import db
    from werkzeug.utils import secure_filename
    experience = Experience.query.all()
    if request.method=="POST":
        experience_date = request.form["time"]
        experience_description=request.form["isyeri"]
        experience_title=request.form["vezife"]
        experience_information=request.form["info"]
        tecrube = Experience(
           experience_date=experience_date,
           experience_description=experience_description,
           experience_title=experience_title,
           experience_information=experience_information
           )
        db.session.add(tecrube)
        db.session.commit()
        return redirect("/")
    return render_template('admin/tecrube.html',experience=experience)
#Delete Experience
@app.route("/experienceDelete/<int:id>",methods=["GET","POST"])
def experience_delete(id):
    from models import Experience
    import os
    from run import db
    exp =   Experience.query.filter_by(id=id).first()
    db.session.delete(exp)
    db.session.commit()
    return redirect ("/admin/experience")
#Update Experience
@app.route("/experienceEdit/<int:id>",methods=["GET","POST"])
def experience_edit(id):
    from models import Experience
    from run import db
    newExperience = Experience.query.filter_by(id=id).first()
    if request.method=="POST":
        exp = Experience.query.filter_by(id=id).first()
        exp.experience_date = request.form["time"]
        exp.experience_title = request.form["isyeri"]
        exp.experience_description = request.form["vezife"]
        exp.experience_information = request.form["info"]
        
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_tecrube.html",newExperience=newExperience)
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
    db.session.delete(edu)
    db.session.commit()
    return redirect ("/admin/education")
#Update Education
@app.route("/educationEdit/<int:id>",methods=["GET","POST"])
def education_edit(id):
    from models import Education
    from run import db
    newEducation = Education.query.filter_by(id=id).first()
    if request.method=="POST":
        edu = Education.query.filter_by(id=id).first()
        edu.education_date = request.form["time"]
        edu.education_title = request.form["derece"]
        edu.education_description = request.form["tehsilqurumu"]
        edu.education_information = request.form["yer"]
        
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_tehsil.html",newEducation=newEducation)
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

# Update Feedback

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

#Portfolio admin
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