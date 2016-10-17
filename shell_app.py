from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mysql@127.0.0.1:3306/coin_data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), unique=True, nullable=False)
    mob_no = db.Column(db.String(10), unique=True, nullable=False)
    complete_registration = db.Column(db.Boolean, nullable=False, default=False)
    gender = db.Column(db.String(6), nullable=False)
    password = db.Column(db.String(16))
    pincode = db.Column(db.Integer)
    timestamp = db.Column(db.Float)
    purchase_id = db.Column(db.Integer, unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), nullable=False)
    mob_no = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text())
    ques = db.Column(db.String(64), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
