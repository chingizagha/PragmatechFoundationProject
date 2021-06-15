from engineers import db
from datetime import datetime



class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20), default='uploads/default.png')
    desc = db.Column(db.Text, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)
    comment = db.relationship('Comment', backref='blog', lazy=True)


    def __repr__(self):
        return f'Blog: {self.title}'

class BlogCategory(db.Model):
    __tablename__ = 'blogcategory'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    category = db.relationship(Blog, backref='blogcategories', lazy=True, cascade='all,delete')

    def __repr__(self):
        return f'Category: {self.title}'

class Testi(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20))
    desc = db.Column(db.Text, nullable=False)

class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    category = db.Column(db.Integer, db.ForeignKey('procategory.id'), nullable=False)

class ProCategory(db.Model):
    __tablename__ = 'procategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.relationship(Project, backref='procategories', lazy=True, cascade='all, delete')


class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)

class Quote(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Worker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    work = db.Column(db.String(25), nullable=False)
    image = db.Column(db.String(20), nullable=True)
    fb_link = db.Column(db.String(250), nullable=True)
    tw_link = db.Column(db.String(250), nullable=True)
    ln_link = db.Column(db.String(250), nullable=True)
    
class Address(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=True)
    desc = db.Column(db.String(50), nullable=False)
    big_desc = db.Column(db.String(75), nullable=False)

class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(75), nullable=False)

class Icon(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(150), nullable=False)

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(32), nullable=False)
    text = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    reply_comment = db.relationship('Reply', backref='comment', lazy=True)

class Reply(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(32), nullable=False)
    text = db.Column(db.String(140), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)


# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     body_html = db.Column(db.Text)
#     path = db.Column(db.Text, index=True)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     disabled = db.Column(db.Boolean)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     parent_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
#     replies = db.relationship('Comment', backref = db.backref('parent',remote_side=[id]),        lazy='dynamic')
#      def save(self):
#        db.session.add(self)
#        db.session.commit()
#        prefix = self.parent.path + '.' if self.parent else ''
#        self.path = prefix + '{:0{}d}'.format(self.id, self._N)
#        db.session.commit()    