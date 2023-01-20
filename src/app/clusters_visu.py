from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import (Arrow, ColumnDataSource, Label,
                          NormalHead, SingleIntervalTicker, TapTool, Tooltip, BoxAnnotation)
from .visu_utils import results_all_periods  #, set_historical_envents
import os
import pandas as pd


class Clusters_Visualization():

    # TODO 
    #def __init__(self, target_word):
    #    self.target_word = target_word

    path = os.getcwd()
    data = results_all_periods(path + "/model_outputs/", tg_word="awful")  # TODO fetch the tg_word from views, before: model_outputs/
    source = ColumnDataSource(data) 

    # TODO change the caption of the third div
    tooltips = """
    <div>
        <span style="font-size: 15px;">@word</span>&nbsp;
    </div>
    <div>
        <span style="font-size: 17px; font-weight: bold;">@Score{0.00}%</span>&nbsp;
    </div>
    <div style="font-size: 11px; color: #666;">semantic shift rate</div>
    """

    TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

    plot = figure(width=1000, height=600,   #x_range=(sprint.MetersBack.max()+2, 0),
                toolbar_location='right', outline_line_color=None,
                y_axis_location="left", tooltips=tooltips)
    plot.y_range.range_padding = 4
    plot.y_range.range_padding_units = "absolute"

    plot.title.text = "Semantic shift of the word awful"  #+ self.target_word   # TODO make it dynamic or just ditch it and use the h4 in the html 
    plot.title.text_font_size = "19px"

    plot.yaxis.ticker = SingleIntervalTicker(interval=10, num_minor_ticks=0)
    #plot.yaxis.axis_line_color = None
    plot.yaxis.major_tick_line_color = None
    plot.ygrid.grid_line_dash = "dashed"
    plot.yaxis.axis_label = "Score"

    plot.xaxis.ticker = [1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020] #[1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020] # TODO adapt it to the time slices 
    plot.xaxis.major_tick_in = -5
    plot.xaxis.major_tick_out = 10
    plot.xgrid.grid_line_color = None
    plot.xaxis.axis_label = "Year"

    time_slice1 = BoxAnnotation(left=1810, right=1860, fill_color='#009E73', fill_alpha=0.1)
    plot.add_layout(time_slice1)
    time_slice2 = BoxAnnotation(left=1960, right=2010, fill_color='#009E73', fill_alpha=0.1)
    plot.add_layout(time_slice2)

    # TODO test for the axis of historical events

    df_hist = pd.read_csv("./historical_events_data/historical_events.csv")  # TODO add events around 1800

    for event in df_hist.values:
        historical_event_label = Label(x=event[1], y=event[2], text=event[0],
                            text_align="center", text_baseline="middle",
                            text_font_size="12px", text_font_style="italic",
                            text_color="lightsalmon")
        plot.add_layout(historical_event_label)
    
    medal = plot.circle(x="Year", y="Score", size='Size', level="overlay",  # size = 10
                        fill_color="Color", line_color="Color", fill_alpha=0.5, source=source)
    plot.hover.renderers = [medal]

    plot.text(x="Year", y="Score", x_offset=15, y_offset=-5,  
            text="word", text_align="left", text_baseline="middle",
            text_font_size="12px", text_color='TextColor', source=source)
    
 

