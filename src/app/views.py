from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from .contact import Contact
from .tool import Analogy

app = Flask(__name__)

app.config.from_object('config')

#init Bootstrap
bootstrap = Bootstrap(app)

#security 
csrf = CSRFProtect(app)


@app.route('/', methods=["GET", "POST"])
@app.route('/index/', methods=["GET", "POST"])
def index():
    form = Analogy()
    if form.validate_on_submit():
        return redirect(url_for('analogy'))
    return render_template('index.html', form=form)

@app.route('/index/tool/', methods=["GET", "POST"])
def tool():
    form = Analogy()
    if form.validate_on_submit():
        return redirect(url_for('analogy'))  # TODO
    return render_template('tool.html', form=form)

@app.route('/analogy/', methods=["GET", "POST"])
def analogy():
    # TODO
    #form = Analogy()
    #if form.validate_on_submit():
        #return redirect(url_for('analogy'))
    return render_template('analogy.html')  

@app.route('/methodology/', methods=["GET", "POST"])
def methodo():
    return render_template('methodology.html')

@app.route('/data/', methods=["GET", "POST"])
def data():
    return render_template('data.html')

@app.route('/contact/', methods=["GET", "POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        return redirect(url_for('contact'))  # TODO indicate to the user that she/he succeded 
    return render_template('contact.html', form=form)