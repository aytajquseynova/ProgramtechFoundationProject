from flask import Flask, render_template
import random
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
       
    )
]        
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",portfolio=portfolio,references=references)
if __name__=="__main__":
    app.run(debug=True)