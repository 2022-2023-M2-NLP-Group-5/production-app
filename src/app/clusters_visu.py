from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import (Arrow, ColumnDataSource, CustomJS, Label,
                          NormalHead, SingleIntervalTicker, TapTool)


fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }
line_color = { "gold": "#c8a850", "silver": "#b0b0b1", "bronze": "#98715d" }

class Clusters_Visualization():
    #def __init__(self, data):
    #    self.source = ColumnDataSource(data)

    data = {"Word": ["awful", "solemn", "majestic", "awe", "dread", "pensive", "gloomy", "horrible", "appalling", "awful", "terrible", "awful", "wonderful", "awful", "weird"], "Year": [1880,1884,1889, 1900,1905,1907, 1920,1922,1927, 1940,1950, 1960,1967, 2000,2001], "Score": [1, 1.5,0.5, 9,9.5, 4,4.5,3.76, 2,2.4, 6.6,6.9,7, 10.1,10.4 ], "Color": [fill_color['gold'], fill_color['gold'], fill_color['gold'], fill_color['gold'], fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold'],fill_color['gold']]}
    source = ColumnDataSource(data)

    tooltips = """
    <div>
        <span style="font-size: 15px;">@Word</span>&nbsp;
    </div>
    <div>
        <span style="font-size: 17px; font-weight: bold;">@Score{0.00}</span>&nbsp;
    </div>
    <div style="font-size: 11px; color: #666;">@{Score}{0.00} meters behind</div>
    """

    plot = figure(width=1000, height=600,   #x_range=(sprint.MetersBack.max()+2, 0),
                toolbar_location=None, outline_line_color=None,
                y_axis_location="left", tooltips=tooltips)
    plot.y_range.range_padding = 4
    plot.y_range.range_padding_units = "absolute"

    plot.title.text = "Semantic shift of the word 'awful'"
    plot.title.text_font_size = "19px"

    plot.xaxis.ticker = SingleIntervalTicker(interval=50, num_minor_ticks=0)
    plot.xaxis.axis_line_color = None
    plot.xaxis.major_tick_line_color = None
    plot.xgrid.grid_line_dash = "dashed"

    plot.yaxis.ticker = [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020]
    plot.yaxis.major_tick_in = -5
    plot.yaxis.major_tick_out = 10
    plot.ygrid.grid_line_color = None

    medal = plot.circle(x="Word", y="Year", size=100, level="overlay",  # MetersBack and Year are the columns from the df 
                        fill_color="Color", line_color="Color", fill_alpha=0.5, source=source)
    plot.hover.renderers = [medal]

    plot.text(x="Score", y="Year", x_offset=10, y_offset=-5,
            text="Word", text_align="left", text_baseline="middle",
            text_font_size="12px", source=source)


    #open_url = CustomJS(args=dict(source=source), code="""
    #source.inspected.indices.forEach(function(index) {
    #    const name = source.data["Word"][index];
    #    const url = "http://en.wikipedia.org/wiki/" + encodeURIComponent(name);
    #    window.open(url);
    #});
    #""")
    #plot.add_tools(TapTool(callback=open_url, renderers=[medal], behavior="inspect"))

    #show(plot)
