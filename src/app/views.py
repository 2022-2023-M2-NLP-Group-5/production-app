from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from .contact import Contact
from .tool import Analogy
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from .clusters_visu import Clusters_Visualization


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
    word = form.input.data

    if form.validate_on_submit():
        return redirect(url_for('analogy', word=word))
    return render_template('index.html', form=form)

@app.route('/analogies/', methods=["GET", "POST"])
def tool():
    form = Analogy()
    word = form.input.data
    if form.validate_on_submit():
        return redirect(url_for('analogy', word=word))  # TODO handle a list of words 
    return render_template('analogies_index.html', form=form)

@app.route('/analogy/<word>/results', methods=["GET", "POST"])
def analogy(word):    
    visu = Clusters_Visualization()
    plot = visu.plot

    script, div = components(plot)

    return render_template('analogy.html',         
        script= script,
        div = div)

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
        return redirect(url_for('contact')) 
    return render_template('contact.html', form=form)