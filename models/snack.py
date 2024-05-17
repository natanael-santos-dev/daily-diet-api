from database import db

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    dateTime = db.Column(db.DateTime)
    check = db.Column(db.Boolean, nullable=False)



