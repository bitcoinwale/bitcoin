from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, \
    PasswordField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, length
from flask_wtf.recaptcha import RecaptchaField  # enabling google recaptcha automatically


class MainForm(Form):       # The first form to be filled by user
    name = StringField('Your Name', validators=[DataRequired(), length(4, 25)])
    # Validators with min and max lenght
    email = StringField('Email', validators=[Email(), length(1, 35)])
    number = StringField('Phone number', validators=[DataRequired(), length(9, 12)])
    # Use of StringField so as to maintain the value of zero infront of the number
    password = PasswordField('Password', validators=[EqualTo('password_confirm'),
                                                     DataRequired(), length(8, 16)])
    # To make the user enter atleast 8 digit long password
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'),
                                           ('female', 'Female'), ('other', 'Other')],
                        validators=[DataRequired()])
    terms = BooleanField('Term & Conditions.', validators=[DataRequired()])
    pincode = IntegerField('Pin Code', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Get Your Purchase ID')


