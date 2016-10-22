from flask_wtf import Form
from wtforms import StringField, DateTimeField, PasswordField, IntegerField,SubmitField
from wtforms.validators import DataRequired


class sign_up(Form):
    email=StringField('Email',validators=[DataRequired()])
    phone=IntegerField('Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Password again',
                                   validators=[Required(), EqualTo('password')])
    submit = SubmitField('Register')
   # otp=IntegerField(('xxxx'), validators=[DataRequired()])


class login(Form):
	username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    token = StringField('Token', validators=[Required(), Length(6, 6)])
    submit = SubmitField('Login')
