from flask import Flask,redirect,url_for,render_template,request
import random
class News:
    def __init__(self, id, title,shortinfo,detail):
        self.id=id
        self.title=title
        self.info=shortinfo
        self.detail=detail
news=[
    News(
        random.randint(1,500),
        'First News Title',
        'shor info about',
        'about detals'
    )
]        
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html', allnews=news)
@app.route("/single")
def single():
    return render_template( 'single.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)