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
    image = db.Column(db.String(20), default='uploads/default.jpeg')
    short_desc = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)

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
    

# USER ==============================

@app.route('/index')
def index():
    blogs = Blog.query.all()[-3:]
    testis = Testi.query.all()[-2:]
    pro_category = Project.query.all()[-4:]
    return render_template('app/index.html', blogs=blogs, testis=testis, pro_category=pro_category) 

@app.route('/about')
def about():
    return render_template('app/about.html')

@app.route('/projects')
def project():
    pro_category = Project.query.all()
    return render_template('app/projects.html', pro_category=pro_category)

@app.route('/testi')
def testi():
    testis = Testi.query.all()
    return render_template('app/testi.html', testis=testis)

@app.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('app/blog.html', blogs=blogs)

@app.route('/contact')
def contact():
    return render_template('app/contact.html')

@app.route('/single/<int:id>')
def single(id):
    blog = Blog.query.get_or_404(id)
    return render_template('app/single-blog.html', blog=blog)

# ADMIN ===============================

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')


# BLOG SECTION =============================

@app.route('/admin/blog')
def blog_list():
    blogs = Blog.query.all()
    blog_category = BlogCategory.query.all()
    return render_template('admin/blog.html', blogs=blogs, blog_category=blog_category)

@app.route('/admin/blog-add', methods=['GET', 'POST'])
def blog_add():
    blog_category = BlogCategory.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            title = request.form['title'],
            name = request.form['name'],
            image = filename,
            short_desc = request.form['short-desc'],
            desc = request.form['desc'],
            category = request.form['category']
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-add.html', blog_category=blog_category)

@app.route('/admin/blog-update/<int:id>', methods=['GET', 'POST'])
def blog_update(id):
    blogs = Blog.query.get_or_404(id)
    blog_category = BlogCategory.query.all()
    if request.method == 'POST':    
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blogs.title = request.form['title']
        blogs.name = request.form['name']
        blogs.short_des = request.form['short-desc']
        blogs.desc = request.form['desc']
        blogs.category = request.form['category']
        blogs.image = filename
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template('admin/blog-update.html', blogs=blogs, blog_category=blog_category)
    
@app.route('/admin/blog-delete/<int:id>', methods=['GET', 'POST'])
def blog_delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog_list'))

@app.route('/admin/blog-cat-list')
def blog_cat_list():
    blog_category = BlogCategory.query.all()
    return render_template('admin/blog-cat-list.html', blog_category=blog_category)

@app.route('/admin/blog-cat-add', methods=['GET', 'POST'])
def blog_cat_add():
    if request.method == 'POST':
        blog_category = BlogCategory(
            title = request.form['title']
        )
        db.session.add(blog_category)
        db.session.commit()
        return redirect(url_for('blog_add'))
    return render_template('admin/blog-cat-add.html')

@app.route('/admin/blog-cat-delete/<int:id>', methods=['GET', 'POST'])
def blog_cat_delete(id):
    blog_category = BlogCategory.query.get_or_404(id)
    db.session.delete(blog_category)
    db.session.commit()
    return redirect(url_for('blog_cat_list'))
   


# =======================================


# PROJECT SECTION =============================

@app.route('/admin/project')
def project_list():
    projects = Project.query.all() 
    return render_template('admin/project.html', projects=projects)

@app.route('/admin/project-add', methods=['GET', 'POST'])
def project_add():
    pro_category = ProCategory.query.all()
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
    return render_template('admin/project-add.html', pro_category=pro_category)

@app.route('/admin/project-update/<int:id>', methods=['GET', 'POST'])
def project_update(id):
    projects = Project.query.get_or_404(id)
    pro_category = ProCategory.query.all()
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        projects.name = request.form['name']
        projects.category = request.form['category']
        projects.image = filename
        db.session.commit()
        return redirect(url_for('project_list'))
    return render_template('admin/project-update.html', projects=projects, pro_category=pro_category)

@app.route('/admin/pro-delete/<int:id>', methods=['GET', 'POST'])
def pro_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('project_list'))


@app.route('/admin/pro-cat-list')
def pro_cat_list():
    pro_category = ProCategory.query.all()
    return render_template('admin/pro-cat-list.html', pro_category=pro_category)

@app.route('/admin/pro-cat-add', methods=['GET', 'POST'])
def pro_cat_add():
    if request.method == 'POST':
        pro_category = ProCategory(
            name = request.form['name']
        )
        db.session.add(pro_category)
        db.session.commit()
        return redirect(url_for('project_add'))
    return render_template('admin/pro-cat-add.html')

@app.route('/admin/pro-cat-delete/<int:id>', methods=['GET', 'POST'])
def pro_cat_delete(id):
    pro_category = ProCategory.query.get_or_404(id)
    db.session.delete(pro_category)
    db.session.commit()
    return redirect(url_for('pro_cat_list'))






# =======================================




# TESTIMONIALS SECTION =============================

@app.route('/admin/testi')
def testi_list():
    testis = Testi.query.all()
    return render_template('admin/testi-list.html', testis=testis)

@app.route('/admin/testi-add', methods=['GET', 'POST'])
def testi_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        testi = Testi(
            name = request.form['name'],
            image = filename,
            desc = request.form['desc']
        )
        db.session.add(testi)
        db.session.commit()
        return redirect(url_for('testi_list'))
    return render_template('admin/testi-add.html')

@app.route('/admin/testi-delete/<int:id>', methods=['GET', 'POST'])
def testi_delete(id):
    testi = Testi.query.get_or_404(id)
    db.session.delete(testi)
    db.session.commit()
    return redirect(url_for('testi_list'))

# =======================================



if __name__ == "__main__":
    app.run(debug=True)