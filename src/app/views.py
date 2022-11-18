from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from .contact import Contact
from .tool import Analogy
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
from .clusters_visu import Clusters_Visualization
from .test_visu import Clusters_Visualization2


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

    #d = {"Word": ["gay", "saaa", "nini", "ibio", "hoih io", "fifioz", "ifofioezhoi", "bfi"], "Year": [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020], "Score": [18, 90, 1920, 40,60,80,20,20]}
    #print(len(d['Word']), len(d['Year']), len(d["Year"])) # Print all of them out here
    #df = pd.DataFrame(d)   
    
    plot = Clusters_Visualization().plot
    plot2 = Clusters_Visualization2().plot

    #plot = figure(title="Résultats",x_axis_label="Date", x_axis_type='datetime', y_axis_label="Note", toolbar_location="above",
    #       plot_width=1200, plot_height=500, sizing_mode="stretch_width", tooltips = TOOLTIPS)
    #plot.line(x,y, line_width= 2)
    #plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))

    script, div = components(plot)
    script2, div2 = components(plot2)
    return render_template('analogy.html',         
        script= script,
        div = div,
        script2 = script2,
        div2 = div2)  

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