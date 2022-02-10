from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import random
import os
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new.db'
db = SQLAlchemy(app)
#about sectionu baslayir
class About:
    def __init__(self,id,name,shortInfo):
        self.id=id
        self.name=name
        self.shortInfo=shortInfo
about=[
     About(
        random.randint(1,500),
        'Mən, Aytac Hüseynova', 
        'Salam, mən Aytac Hüseynova. 20 yaşım var. Azərbaycan Dövlət Neft və Sənaye Universiteti SABAH fakültəsi Proseslərin avtomatlaşdırılması mühəndisliyində 4-cü kurs tələbəsiyəm. Eyni zamanda "Pragmatech Education" kursu vasitəsilə development sahəsi üzrə təhsil alıram. Məqsədim Front-End Developer olmaqdır.')
        ]
#about sectionu bitir
#skills sectionu baslayir
class Skill:
    def __init__(self,id,icon):
        self.id=id
        self.icon=icon
skill=[
    Skill(
        random.randint(1, 500),
        "fab fa-html5",  
    ),
    Skill(
           random.randint(1, 500),
        "fab fa-css3-alt",
    ),
     Skill(
           random.randint(1, 500),
        "fab fa-js-square",
    ),
      Skill(
           random.randint(1, 500),
        "fab fa-python",
    ),
        Skill(
           random.randint(1, 500),
        "fab fa-github",
    ),
         ]
#skills sectionu bitir
#work classi baslayir
class Work:
    def __init__(self,id,time,place, job, shortInfo):
        self.id=id
        self.time=time
        self.place=place
        self.job=job
        self.shortInfo=shortInfo
work=[
    Work(
        random.randint(1,500),
        "JANUARY, 2013 - PRESENT",
        "Flash media inc.",
        "SENIOR UX/UI DESIGNER",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    ),
      Work(
        random.randint(1,500),
        "MARCH'11 - DECEMBER'12",
        "Codedash Studio",
        "UX DESIGNER<",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    ),
       Work(
        random.randint(1,500),
        "JULY'09 - APRIL'11",
        "Foursqure Studio",
        "VISUAL / UI DESIGNER",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    )
      
    
    ]
#work classin sonu
#education classi baslayir
class Education:
    def __init__(self,id,time,place, job, shortInfo):
        self.id=id
        self.time=time
        self.place=place
        self.job=job
        self.shortInfo=shortInfo
education=[
    Education(
        random.randint(1,500),
        "JANUARY, 2007",
        "Master Degree Of Design",
        "UNIVERSITY OF DESIGN",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    ),
      Education(
        random.randint(1,500),
        "JUNE, 2004",
        "Bachelor Of Arts",
        "UNIVERSITY OF DESIGN",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    ),
       Education(
        random.randint(1,500),
        "JANUARY, 2001",
        "Master Degree Of Design",
        "VISUAL / UI DESIGNER",
        " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit maxime laborum sequi,magni earum quo soluta sintvelit numquam, ipsum illum! Nostrum possimus illo architecto praesentium ut aliquam dolorem"
    )
      
    
    ]
#education classi sonu
#portfolio sectionu baslayir
class Portfolio:
    def __init__(self, id, icon,projectname,img,):
        self.id=id
        self.icon=icon
        self.projectname=projectname
        self.img=img
portfolio=[
    Portfolio(
        random.randint(1,500),
        "fa fa-image",
        "Project Name",
        "https://i.pinimg.com/474x/b4/3c/0b/b43c0b0d65e7500b6f95222ae5021835.jpg"
    ),
    Portfolio(
        random.randint(1,500),
        "fa fa-image",
        "Project Name",
        "https://i.pinimg.com/474x/b4/3c/0b/b43c0b0d65e7500b6f95222ae5021835.jpg"
        
    )
] 
#portfolio sectionu bitir
#references sectionu baslayir 

# Feedback
class Feedbacks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    feedback_img = db.Column(db.String(100))
    feedback_rey = db.Column(db.String(100))
    feedback_cmntrname = db.Column(db.String(100))
    feedback_cmntrjob = db.Column(db.String(100))

@app.route("/admin/feedbacks",methods=["GET","POST"])
def feedback():
    from werkzeug.utils import secure_filename
    feedbacks = Feedbacks.query.all()
    if request.method=="POST":
        file = request.files['img']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
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



#references sectionu bitir   
@app.route("/")
def index():
    feed = Feedbacks.query.all()
    return render_template("app/index.html", feed=feed)

@app.route("/admin")
def admin():
    return render_template('admin/base.html')

@app.route("/admin/skill")
def skill():
    return render_template('admin/skill.html')

@app.route("/admin/tehsil")
def tehsil():
    return render_template('admin/tehsil.html')
@app.route("/admin/tecrube")
def tecrube():
    return render_template('admin/tecrube.html')

if __name__=="__main__":
    # db.create_all()
    app.run(debug=True)