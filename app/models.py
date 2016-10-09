from app import db


class User(db.Model):
    __tablename__ = 'Sign_In'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), unique=True, nullable=False)
    mob_no = db.Column(db.String(10), unique=True, nullable=False)
    complete_registration = db.Column(db.Boolean, nullable=False, default=True)
    password = db.Column(db.String(16))
    purchase_id = db.Column(db.Integer)

