from logging import debug
import re
from werkzeug.datastructures import RequestCacheControl
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname, realpath, os
from sqlalchemy.orm import backref
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20))

    def __repr__(self):
        return f'Blog: {self.title}'

class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20))

    

@app.route('/index')
def index():
    blogs = Blog.query.all()
    return render_template('app/index.html', blogs=blogs) 

@app.route('/about')
def about():
    return render_template('app/about.html')

@app.route('/projects')
def project():
    return render_template('app/projects.html')

@app.route('/testi')
def testi():
    return render_template('app/testi.html')

@app.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('app/blog.html', blogs=blogs)

@app.route('/contact')
def contact():
    return render_template('app/contact.html')

@app.route('/single')
def single():
    return render_template('app/single-blog.html')

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/admin/blog')
def blog_list():
    blogs = Blog.query.all()
    return render_template('admin/blog.html', blogs=blogs)

@app.route('/admin/blog-add', methods=['GET', 'POST'])
def blog_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            title = request.form['title'],
            name = request.form['name'],
            image = filename,
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-add.html')

@app.route('/admin/blog-update')
def blog_update():
    blogs = Blog.query.all()
    return render_template('admin/blog-update.html', blogs=blogs)
    

@app.route('/admin/project')
def project_list():
    projects = Project.query.all() 
    return render_template('admin/project.html', projects=projects)

@app.route('/admin/project-add', methods=['GET', 'POST'])
def project_add():
    if request.method=='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        project = Project(
            category = request.form['category'],
            name = request.form['name'],
            image = filename
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('project_list'))
    return render_template('admin/project-add.html')

@app.route('/admin/project-update')
def project_update():
    projects = Project.query.all()
    return render_template('admin/project-update.html', projects=projects)







if __name__ == "__main__":
    app.run(debug=True)