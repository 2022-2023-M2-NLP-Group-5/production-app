from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import (Arrow, ColumnDataSource, Label,
                          NormalHead, SingleIntervalTicker, TapTool)
from .visu_utils import results_all_periods

import os

#fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }
#line_color = { "gold": "#c8a850", "silver": "#b0b0b1", "bronze": "#98715d" }

class Clusters_Visualization():

    # TODO 
    #def __init__(self, target_word):
    #    self.target_word = target_word

    path = os.getcwd()
    data = results_all_periods(path + "/")
    source = ColumnDataSource(data) 

    # TODO change the caption of the third div
    tooltips = """
    <div>
        <span style="font-size: 15px;">@word</span>&nbsp;
    </div>
    <div>
        <span style="font-size: 17px; font-weight: bold;">@Score{0.00}</span>&nbsp;
    </div>
    <div style="font-size: 11px; color: #666;">@{Score}{0.00} semantic shift</div>
    """

    plot = figure(width=1000, height=600,   #x_range=(sprint.MetersBack.max()+2, 0),
                toolbar_location=None, outline_line_color=None,
                y_axis_location="left", tooltips=tooltips)
    plot.y_range.range_padding = 4
    plot.y_range.range_padding_units = "absolute"

    plot.title.text = "Semantic shift of the word "  #+ self.target_word   # TODO make it dynamic
    plot.title.text_font_size = "19px"

    plot.yaxis.ticker = SingleIntervalTicker(interval=50, num_minor_ticks=0)
    #plot.yaxis.axis_line_color = None
    plot.yaxis.major_tick_line_color = None
    plot.ygrid.grid_line_dash = "dashed"
    plot.yaxis.axis_label = "Score"

    plot.xaxis.ticker = [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020]
    plot.xaxis.major_tick_in = -5
    plot.xaxis.major_tick_out = 10
    plot.xgrid.grid_line_color = None
    plot.xaxis.axis_label = "Year"

    medal = plot.circle(x="Year", y="Score", size=10, level="overlay", 
                        fill_color="Color", line_color="Color", fill_alpha=0.5, source=source)
    plot.hover.renderers = [medal]

    plot.text(x="Year", y="Score", x_offset=10, y_offset=-5,  
            text="word", text_align="left", text_baseline="middle",
            text_font_size="12px", source=source)
