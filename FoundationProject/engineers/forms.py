from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 

'''Contactform is used on the contact.html page and allows you to send requests''' 
class ContactForm(FlaskForm):

    first_name = StringField('First name', validators=[DataRequired(), Length(min=3, max=40)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
    submit = SubmitField('SEND MESSAGE')
    
'''Quoteform is used on the index.html page and allows you to send requests''' 
class QuoteForm(FlaskForm):

    name = StringField('Your name', validators=[DataRequired(), Length(min=3, max=40)], render_kw={"placeholder": "Your Name"})
    phone = StringField('Phone Number', validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
    email = StringField('Your Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    subject = StringField('Subject', validators=[DataRequired()], render_kw={"placeholder": "Subject"})
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)], render_kw={"placeholder": "Message"})
    submit = SubmitField('SEND MESSAGE')

'''CommentForm is used on the single.html page and allows you add comments below the blogs''' 
class CommentForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    text = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=200)])
    date = DateField('Posted Date', format='%d-%m-%Y')
    submit = SubmitField('POST COMMENT')

class TagForm(FlaskForm):
    title = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Add')

    