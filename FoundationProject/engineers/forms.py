from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 


class ContactForm(FlaskForm):

    first_name = StringField('First name', validators=[DataRequired(), Length(min=3, max=40)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
    submit = SubmitField('SEND MESSAGE')