from flask import Flask, render_template
import random
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
class References:
    def __init__(self,id, rey,img,cmntrname, cmntrjob):
        self.id=id
        self.rey=rey
        self.img=img
        self.cmntrname=cmntrname
        self.cmntrjob=cmntrjob
references=[
    References(
        random.randint(1,500),
       '"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit mlaborum sequi, magni earum quo soluta sint velit numquam, ipsum illum! Npossimus illo architecto praesentium ut aliquam dolorem."',
       "http://themeelite.com/demos/flatr/img/referance1@2x.jpg",
       "Gulsen Zalova",
       'Front-End Developer'
       ),
     References(
        random.randint(1,500),
       '"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit m   laborum sequi, magni earum quo soluta sint velit numquam, ipsum illum! N possimus illo architecto praesentium ut aliquam dolorem."',
       "http://themeelite.com/demos/flatr/img/referance2@2x.jpg",
       "Emil Abdullayev",
       'Back-End Developer'
       ),
     
]     
#references sectionu bitir   
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("app/index.html",about=about,skill=skill,work=work,education=education,portfolio=portfolio,references=references )

@app.route("/admin")
def admin():
    return render_template('admin/base.html')

@app.route("/admin/feedbacks")
def feedback():
    return render_template('admin/feedbacks.html')

@app.route("/admin/tehsil")
def tehsil():
    return render_template('admin/tehsil.html')
@app.route("/admin/tecrube")
def tecrube():
    return render_template('admin/tecrube.html')

if __name__=="__main__":
    app.run(debug=True)