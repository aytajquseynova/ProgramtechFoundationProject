from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import os

app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

#app routes
from app.routes import *

#admin routes
from admin.routes import *

if __name__=="__main__":
    # db.create_all()
    app.run(debug=True)