from engineers import db
from datetime import datetime


'''Blog model contains the blogs of the site and is related to the BlogCategory model'''
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20), default='uploads/default.png')
    desc = db.Column(db.Text, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)
    comment = db.relationship('Comment', backref='blog', lazy=True, cascade='all, delete')
    tag = db.relationship('Tag', secondary='blogs_tags', backref=db.backref('blog', lazy='dynamic'))


    def __repr__(self):
        return f'Blog: {self.title}'

'''BlogCategory model is in relationship 
   with Blog model and contains category types'''
class BlogCategory(db.Model):
    __tablename__ = 'blogcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    category = db.relationship('Blog', backref='blogcategories', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f'Category: {self.title}'
    
'''Testi model contains the testimonials of the site'''
class Testi(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20))
    desc = db.Column(db.Text, nullable=False)

'''Project model contains the projects of the site and is related to the ProjectCategory model'''
class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('procategory.id'), nullable=False)

'''ProCategory model is in relationship 
   with Project model and contains category types'''
class ProCategory(db.Model):
    __tablename__ = 'procategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.relationship(Project, backref='procategories', lazy=True, cascade='all, delete')

'''Contact model contains the queries received on the site'''
class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)

'''Quote model contains the queries received on the site'''
class Quote(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
'''Worker model contains the information about workers of the company'''
class Worker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    work = db.Column(db.String(25), nullable=False)
    image = db.Column(db.String(20), nullable=True)
    fb_link = db.Column(db.String(250), nullable=True)
    tw_link = db.Column(db.String(250), nullable=True)
    ln_link = db.Column(db.String(250), nullable=True)

'''Address model contains the address of the company'''
class Address(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=True)
    desc = db.Column(db.String(50), nullable=False)
    big_desc = db.Column(db.String(75), nullable=False)

'''Card model stores information in the form of a card on the site'''
class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(75), nullable=False)


'''Comment model contains the comments received on the site'''
class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(32), nullable=False)
    text = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)

class Tag(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    db.column = db.relationship(Blog, backref='tags', lazy=True)


blogs_tags = db.Table('blogs_tags',
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))
