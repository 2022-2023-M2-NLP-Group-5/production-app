from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from .contact import Contact
from .tool import Analogy
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from .clusters_visu import Clusters_Visualization
#from .tree_visu import TreeVisu
from .table_visu import table_visu, table_display
from .visu_utils import results_all_periods
import os


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
    language = form.language.data

    if form.validate_on_submit():
        return redirect(url_for('analogy', word=word, lang=language))
    return render_template('index.html', form=form)

@app.route('/analogies/', methods=["GET", "POST"])
def tool():
    form = Analogy()
    word = form.input.data
    language = form.language.data
    headings, data = table_display()

    if form.validate_on_submit():
        return redirect(url_for('analogy', word=word, lang=language))
    return render_template('analogies_index.html', form=form, data=data, headings=headings)

@app.route('/analogy/<word>/<lang>/results', methods=["GET", "POST"])
def analogy(word, lang):
    # For the table of results 
    headings, data = table_visu(word)

    path = os.getcwd()
    data_csv = results_all_periods(path + "/model_outputs/", word, lang)

    # For the cluster visualization    
    visu_cluster = Clusters_Visualization(word, lang, data_csv)
    plot_cluster = visu_cluster.plot()


    script, div = components(plot_cluster)

    # Fetch the visualization mode 
    visu_mode = request.args.get('visu_mode', "tree", type=str)
    print("Visu mode", visu_mode)

    return render_template('analogy.html',        
        script= script,
        div = div,
        word=word, 
        visu_mode=visu_mode, 
        headings=headings,
        data=data, 
        lang = lang)

@app.route('/methodology/', methods=["GET", "POST"])
def methodo():
    return render_template('methodology.html')

@app.route('/data/', methods=["GET", "POST"])
def data():
    data_en = pd.read_csv("./words_data/generated_words_en.csv")
    data_de = pd.read_csv("./words_data/generated_words_de.csv")

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