from flask import Flask, render_template

app=Flask(__name__)
detallar=[
  'Aytac',
  'Huseynova',
  '20 yas'
]
@app.route('/')
def home():
     return render_template('index.html', data=detallar)
  
@app.route("/about")
def page():
  return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)