from app import db


class User(db.model):
    __tablename__ = 'Sign_In'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email_id = db.Column(db.String, unique=True, nullable=False)
    mob_no = db.Column(db.Integer, unique=True, nullable=False)
    complete_registration = db.Column(db.Boolean)
    