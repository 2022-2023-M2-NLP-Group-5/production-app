from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from .contact import Contact
from .tool import Analogy
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from .clusters_visu import Clusters_Visualization
from .tree_visu import TreeVisu


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
    # For the tree visualization
    visu_tree = TreeVisu()
    plot_tree = visu_tree.plot
    script_tree, div_tree = components(plot_tree)

    # For the cluster visualization    
    visu_cluster = Clusters_Visualization()
    plot_cluster = visu_cluster.plot

    script, div = components(plot_cluster)

    # Fetch the visualization mode 
    visu_mode = request.args.get('visu_mode', "tree", type=str)
    print("Visu mode", visu_mode)

    return render_template('analogy.html', 
        script_tree = script_tree,
        div_tree = div_tree,        
        script= script,
        div = div,
        word=word, 
        visu_mode=visu_mode)

@app.route('/methodology/', methods=["GET", "POST"])
def methodo():
    return render_template('methodology.html')

@app.route('/data/', methods=["GET", "POST"])
def data():
    # TODO do a prettier thing
    data_en = pd.read_csv("./words_data/coha_sample.csv")
    data_de = pd.read_csv("./words_data/semeval_words_de.csv")

    words_en = data_en 
    words_de = data_de 
    
    return render_template('data.html',tables_en=[words_en.to_html(classes='word')],
        tables_de=[words_de.to_html(classes='word')],
        titles = ['na', 'Word'])

@app.route('/contact/', methods=["GET", "POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        return redirect(url_for('contact')) 
    return render_template('contact.html', form=form)