from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 


class ContactForm(FlaskForm):

    first_name = StringField('First name', validators=[DataRequired(), Length(min=3, max=40)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
    submit = SubmitField('SEND MESSAGE')

class QuoteForm(FlaskForm):

    name = StringField('Your name', validators=[DataRequired(), Length(min=3, max=40)], render_kw={"placeholder": "Your Name"})
    phone = StringField('Phone Number', validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
    email = StringField('Your Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    subject = StringField('Subject', validators=[DataRequired()], render_kw={"placeholder": "Subject"})
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)], render_kw={"placeholder": "Message"})
    submit = SubmitField('SEND MESSAGE')

class CommentForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    text = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
    date = DateField('Posted Date', format='%d-%m-%Y')
    submit = SubmitField('POST COMMENT')

# class ReplyForm(FlaskForm):

#     name = StringField('Name', validators=[DataRequired(), Length(min=3, max=15)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     reply = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
#     submit = SubmitField('POST COMMENT')

    