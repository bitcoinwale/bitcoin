from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, length, optional
from flask_wtf.recaptcha import RecaptchaField


class QueryForm(Form):
    name = StringField('Your Name', validators=[DataRequired(), length(4, 25)])
    email = StringField('Email', validators=[Email(), length(1, 35)])
    number = StringField('Phone number', validators=[DataRequired(), length(9, 12)])
    query = StringField('Your Query', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[optional()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send your query')
