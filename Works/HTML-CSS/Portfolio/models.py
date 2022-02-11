from run import db
#Tehsil
class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_date = db.Column(db.String(100))
    education_title= db.Column(db.String(100))
    education_description = db.Column(db.String(100))
    education_information = db.Column(db.String(100))
    

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