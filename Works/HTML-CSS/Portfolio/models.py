from run import db
from enum import unique
from flask_login.mixins import UserMixin
#Tehsil
class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_date = db.Column(db.String(100))
    education_title= db.Column(db.String(100))
    education_description = db.Column(db.String(100))
    education_information = db.Column(db.String(100))
#Experince
class Experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    experience_date = db.Column(db.String(100))
    experience_title= db.Column(db.String(100))
    experience_description = db.Column(db.String(100))
    experience_information = db.Column(db.String(100))
# Feedback
class Feedbacks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    feedback_img = db.Column(db.String(100))
    feedback_rey = db.Column(db.String(100))
    feedback_cmntrname = db.Column(db.String(100))
    feedback_cmntrjob = db.Column(db.String(100))
    
#Portfolio  
class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_img = db.Column(db.String(100))
    portfolio_title = db.Column(db.String(100))
    
#Contact    
class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_name = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    contact_subject = db.Column(db.String(100))
    contact_message = db.Column(db.String(100))
    
# Login
class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)
    