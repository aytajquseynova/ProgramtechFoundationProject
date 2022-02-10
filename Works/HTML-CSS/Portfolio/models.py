from app import db

# Feedback
class Feedbacks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    feedback_img = db.Column(db.String(100))
    feedback_rey = db.Column(db.String(100))
    feedback_cmntrname = db.Column(db.String(100))
    feedback_cmntrjob = db.Column(db.String(100))