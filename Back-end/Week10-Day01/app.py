from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('app/index.html') 

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