from app.utils.database import db

class Animal(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  species = db.Column(db.String(100), nullable = True)
  gender = db.Column(db.String(100), nullable = False)
