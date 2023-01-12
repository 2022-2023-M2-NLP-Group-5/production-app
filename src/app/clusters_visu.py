from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import (Arrow, ColumnDataSource, Label,
                          NormalHead, SingleIntervalTicker, TapTool)
from .visu_utils import results_all_periods
import os


class Clusters_Visualization():

    # TODO 
    #def __init__(self, target_word):
    #    self.target_word = target_word

    path = os.getcwd()
    data = results_all_periods(path + "/", tg_word="awful")  # TODO fetch the tg_word from views 
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

    TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

    plot = figure(width=1000, height=600,   #x_range=(sprint.MetersBack.max()+2, 0),
                toolbar_location='right', outline_line_color=None,
                y_axis_location="left", tooltips=tooltips)
    plot.y_range.range_padding = 4
    plot.y_range.range_padding_units = "absolute"

    plot.title.text = "Semantic shift of the word awful"  #+ self.target_word   # TODO make it dynamic
    plot.title.text_font_size = "19px"

    plot.yaxis.ticker = SingleIntervalTicker(interval=10, num_minor_ticks=0)
    #plot.yaxis.axis_line_color = None
    plot.yaxis.major_tick_line_color = None
    plot.ygrid.grid_line_dash = "dashed"
    plot.yaxis.axis_label = "Score"

    plot.xaxis.ticker = [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020]
    plot.xaxis.major_tick_in = -5
    plot.xaxis.major_tick_out = 10
    plot.xgrid.grid_line_color = None
    plot.xaxis.axis_label = "Year"

    medal = plot.circle(x="Year", y="Score", size='Size', level="overlay",  # size = 10
                        fill_color="Color", line_color="Color", fill_alpha=0.5, source=source)
    plot.hover.renderers = [medal]

    plot.text(x="Year", y="Score", x_offset=15, y_offset=-5,  
            text="word", text_align="left", text_baseline="middle",
            text_font_size="12px", text_color='TextColor', source=source)
