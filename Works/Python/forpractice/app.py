from flask import Flask, render_template

app=Flask(__name__)
telebeler=[
  {'ad':'Aytac',
   'soyad':'Huseynova',
   'yas':'20'},
  
  {'ad':'Sebine',
   'soyad':'Huseynova',
   'yas':'23'},
  {'ad':'Eli',
   'soyad':'huseynov',
   'yas':'17'}
]
@app.route('/')
def home():
     return render_template('index.html', data=telebeler)
  
@app.route("/about")
def page():
  return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)