from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import os
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"

#app routes
from app.routes import *

#admin routes
from admin.routes import *

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)