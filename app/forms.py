from flask_wtf import Form
from wtforms import StringField, DateTimeField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class sign_up(Form):
    email=StringField('Email',validators=[DataRequired()])
    phone=IntegerField('Number', validators=[DataRequired()])
    otp=IntegerField(('xxxx'), validators=[DataRequired()])


class login(Form):
	phone=IntegerField('Number', validators=[DataRequired()])
	otp=IntegerField('xxxx', validators=[DataRequired()])
	