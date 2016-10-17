from . import db


class User(db.Model):
    __tablename__ = 'Sign_In'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), unique=True, nullable=False)
    mob_no = db.Column(db.String(10), unique=True, nullable=False)
    complete_registration = db.Column(db.Boolean, nullable=False, default=False)
    gender = db.Column(db.String(6), nullable=False)
    password = db.Column(db.String(16))
    pincode = db.Column(db.Integer)
    timestamp = db.Column(db.Float)
    purchase_id = db.Column(db.Integer, unique=True)


class Contact(db.Model):
    __tablename__ = 'Queries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), nullable=False)
    mob_no = db.Column(db.String(10), nullable=False)
    ques = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text())
