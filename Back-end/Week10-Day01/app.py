from logging import debug
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20))

    def __repr__(self):
        return f'Blog: {self.title}'

    

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
    return render_template('app/blog.html')

@app.route('/contact')
def contact():
    return render_template('app/contact.html')

@app.route('/single')
def single():
    return render_template('app/single-blog.html')



if __name__ == "__main__":
    app.run(debug=True)