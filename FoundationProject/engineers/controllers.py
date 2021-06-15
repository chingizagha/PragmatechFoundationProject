from flask.helpers import flash
from engineers import app, os, db
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from engineers.models import Blog, BlogCategory, Project, ProCategory, Testi, Contact, Quote, Worker, Address, Comment, Reply, Card
from engineers.forms import ContactForm, QuoteForm, CommentForm



# USER ==============================

@app.route('/index', methods=['GET', 'POST'])
def index():
    address = Address.query.all()
    card = Card.query.all()
    blogs = Blog.query.all()[-3:]
    testis = Testi.query.all()[-2:]
    pro_category = Project.query.all()[-4:]
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(
            name = form.name.data,
            phone = form.phone.data,
            email = form.email.data,
            subject = form.subject.data,
            message = form.message.data
        )
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('app/index.html', blogs=blogs, testis=testis, pro_category=pro_category, form=form, address=address, card=card) 

@app.route('/about')
def about():
    address = Address.query.all()
    workers = Worker.query.all()
    return render_template('app/about.html', workers=workers, address=address)

@app.route('/projects')
def project():
    address = Address.query.all()
    pro_category = Project.query.all()
    return render_template('app/projects.html', pro_category=pro_category, address=address)

@app.route('/testi')
def testi():
    testis = Testi.query.all()
    address = Address.query.all()
    return render_template('app/testi.html', testis=testis, address=address)

@app.route('/blog')
def blog():
    blogs = Blog.query.all()
    address = Address.query.all()
    return render_template('app/blog.html', blogs=blogs, address=address)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    address = Address.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            phone = form.phone.data,
            message = form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contact'))
    return render_template('app/contact.html', form=form, address=address)

# @app.route('/single/<id>')
# def single(id):
#     address = Address.query.all()
#     comment = Comment.query.filter_by(blog_id=id)
#     blog = Blog.query.get_or_404(id)
#     form = CommentForm()
#     return render_template('app/single-blog.html', blog=blog, address=address, comment=comment, form=form)

# @app.route('/addcomment/<id>', methods=['GET', 'POST'])
# def addcomment(id):
#     blog = Blog.query.get_or_404(id)
#     comment = Comment.query.filter_by(blog_id=id)
#     address = Address.query.all()
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = Comment(
#             author = form.name.data,
#             mail = form.email.data,
#             text = form.text.data,
#             timestamp = form.date.data,
#             blog_id = id
#         )
#         db.session.add(comment)
#         db.session.commit()
#         return redirect(url_for('blog'))
#     return render_template('app/single-blog.html', blog=blog,  address=address, form=form, comment=comment)


@app.route('/single/<id>', methods=['GET', 'POST'])
def single(id):
    address = Address.query.all()
    comment = Comment.query.filter_by(blog_id=id)
    reply = Reply.query.filter_by(comment_id=id)
    blog = Blog.query.get_or_404(id)
    form = CommentForm()
    category = BlogCategory.query.all()
    if form.validate_on_submit():
        comment = Comment(
            author = form.name.data,
            mail = form.email.data,
            text = form.text.data,
            timestamp = form.date.data,
            blog_id = id
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('single', id=id))
    # elif form.validate_on_submit():
    #     reply = Reply(
    #         author = form.name.data,
    #         mail = form.email.data,
    #         text = form.text.data,
    #         timestamp = form.date.data,
    #         comment_id = id
    #     )
    #     db.session.add(reply)
    #     db.session.commit()
    #     return redirect(url_for('single', id=id))
    return render_template('app/single-blog.html', blog=blog, address=address, comment=comment, form=form, category=category, reply=reply)


    # blog = Blog.query.get_or_404(id)
    # address = Address.query.all()
    # form = CommentForm()
    # if form.validate_on_submit():
    #     comment = Comment(
    #         author = form.name.data,
    #         mail = form.email.data,
    #         text = form.text.data,
    #         timestamp = form.date.data,
    #         blog_id = id
    #     )
    #     db.session.add(comment)
    #     db.session.commit()
    #     return redirect(url_for('blog'))
    # return render_template('app/single-blog.html', blog=blog,  address=address, form=form, comment=comment)
    

# ADMIN ===============================

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

# =======================================

# INCLUDES SECTION =============================

@app.route('/index')
def navbar():
    address = Address.query.all()
    return render_template('includes/header.html', address=address)





# =======================================

# HOME SECTION =============================

    # QUOTE SECTION

@app.route('/admin/quote')
def quote_info():
    quotes = Quote.query.all()
    return render_template ('admin/quote.html', quotes=quotes)

@app.route('/admin/quote-delete/<int:id>', methods=['GET', 'POST'])
def quote_delete(id):
    quote = Quote.query.get_or_404(id)
    db.session.delete(quote)
    db.session.commit()
    return redirect(url_for('quote_info'))

# ==========

    # ADDRESS SECTION

@app.route('/admin/address')
def address_info():
    address = Address.query.all()
    return render_template('admin/address.html', address=address)

@app.route('/admin/address-add', methods=['GET', 'POST'])
def address_add():
    if request.method == 'POST':
        address = Address(
            icon = request.form['icon'],
            desc = request.form['desc'],
            big_desc = request.form['big_desc']
        )
        db.session.add(address)
        db.session.commit()
        return redirect(url_for('address_info'))
    return render_template('admin/address-add.html')

@app.route('/admin/address-update/<int:id>', methods=['GET', 'POST'])
def address_update(id):
    address = Address.query.get_or_404(id)
    if request.method == 'POST':
        address.icon = request.form['icon']
        address.desc = request.form['desc']
        address.big_desc = request.form['big_desc']
        db.session.commit()
        return redirect(url_for('address_info'))
    return render_template('admin/address-update.html', address=address)

@app.route('/admin/address-delete/<int:id>', methods=['GET', 'POST'])
def address_delete(id):
    address = Address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()
    return redirect(url_for('address_info'))

# ==========

    # CARD SECTION

@app.route('/admin/card')
def card_info():
    card = Card.query.all()
    return render_template('admin/card.html', card=card)

@app.route('/admin/card-add', methods=['GET', 'POST'])
def card_add():
    if request.method == 'POST':
        card = Card(
            icon = request.form['icon'],
            title = request.form['title'],
            desc = request.form['desc']
        )
        db.session.add(card)
        db.session.commit()
        return redirect(url_for('card_info'))
    return render_template('admin/card-add.html')

@app.route('/admin/card-update/<int:id>', methods=['GET', 'POST'])
def card_update(id):
    card = Card.query.get_or_404(id)
    if request.method == 'POST':
        card.icon = request.form['icon']
        card.desc = request.form['title']
        card.big_desc = request.form['desc']
        db.session.commit()
        return redirect(url_for('card_info'))
    return render_template('admin/card-update.html', card=card)

@app.route('/admin/card-delete/<int:id>', methods=['GET', 'POST'])
def card_delete(id):
    card = Card.query.get_or_404(id)
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('card_info'))



# =======================================

# ABOUT US SECTION =============================

@app.route('/admin/worker')
def worker_list():
    workers = Worker.query.all()
    return render_template('admin/worker.html', workers=workers)

@app.route('/admin/worker-add', methods=['GET', 'POST'])
def worker_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        worker = Worker(
            name = request.form['name'],
            work = request.form['work'],
            fb_link = request.form['fb'],
            tw_link = request.form['tw'],
            ln_link = request.form['ln'],
            image = filename
        )
        db.session.add(worker)
        db.session.commit()
        return redirect(url_for('worker_list'))
    return render_template('admin/worker-add.html')

@app.route('/admin/worker-update/<int:id>', methods=['GET', 'POST'])
def worker_update(id):
    workers = Worker.query.get_or_404(id)
    if request.method == 'POST':    
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        workers.name = request.form['name']
        workers.work = request.form['work']
        workers.fb_link = request.form['fb']
        workers.tw_link = request.form['tw']
        workers.ln_link = request.form['ln']
        workers.image = filename
        db.session.commit()
        return redirect(url_for('worker_list'))
    return render_template('admin/worker-update.html', workers=workers)
    
@app.route('/admin/worker-delete/<int:id>', methods=['GET', 'POST'])
def worker_delete(id):
    worker = Worker.query.get_or_404(id)
    db.session.delete(worker)
    db.session.commit()
    return redirect(url_for('worker_list'))


# =======================================

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

# CONTACT SECTION =============================

@app.route('/admin/contact')
def contact_info():
    contacts = Contact.query.all()
    return render_template ('admin/contact.html', contacts=contacts)

@app.route('/admin/contact-delete/<int:id>', methods=['GET', 'POST'])
def contact_delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contact_info'))
# =======================================