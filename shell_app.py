from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mysql@127.0.0.1:3306/buy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Sign_In'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email_id = db.Column(db.String(64), unique=True, nullable=False)
    mob_no = db.Column(db.String(10), unique=True, nullable=False)
    complete_registration = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(16))
    purchase_id = db.Column(db.Integer)


if __name__ == "__main__":
    app.run()
