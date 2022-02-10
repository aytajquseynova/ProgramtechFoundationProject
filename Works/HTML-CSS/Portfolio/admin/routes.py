import flask
from app import app 
from flask import Flask,render_template,url_for,redirect,request

# Admin Feedbacks
@app.route("/admin/feedbacks",methods=["GET","POST"])
def feedback():
    from models import Feedbacks
    import os
    from app import db
    from werkzeug.utils import secure_filename
    feedbacks = Feedbacks.query.all()
    if request.method=="POST":
        file = request.files['img']
        filename = secure_filename(file.filename)  
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        feedback_rey = request.form["rey"]
        feedback_cmntrname=request.form["cmntrname"]
        feedback_cmntrjob=request.form["cmntrjob"]
        print(feedback_rey)
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
    from app import db
    feedbacks = Feedbacks.query.filter_by(id=id).first()
    filename = feedbacks.feedback_img
    os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    db.session.delete(feedbacks)
    db.session.commit()
    return redirect ("/admin/feedbacks")
