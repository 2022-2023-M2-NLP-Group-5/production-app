from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import (ColumnDataSource, Label,
                          SingleIntervalTicker, BoxAnnotation)
from .visu_utils import results_all_periods
import os
import pandas as pd


class Clusters_Visualization():

    def __init__(self, queried_word, lang, data):
        self.queried_word = queried_word
        self.lang = lang
        self.data = data

    def plot(self):
        source = ColumnDataSource(self.data) 

        tooltips = """
        <div>
            <span style="font-size: 15px;">@word</span>&nbsp;
        </div>
        <div>
            <span style="font-size: 17px; font-weight: bold;">@Score{0.00}</span>&nbsp;
        </div>
        <div style="font-size: 11px; color: #666;">semantic shift rate</div>
        """

        TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

        plot = figure(width=1000, height=600, 
                    toolbar_location='right', outline_line_color=None,
                    y_axis_location="left", tooltips=tooltips)
        plot.y_range.range_padding = 4
        plot.y_range.range_padding_units = "absolute"

        plot.yaxis.ticker = SingleIntervalTicker(interval=10, num_minor_ticks=0)
        plot.yaxis.major_tick_line_color = None
        plot.ygrid.grid_line_dash = "dashed"
        plot.yaxis.axis_label = "Score"

        plot.xaxis.ticker = [1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020]
        plot.xaxis.major_tick_in = -5
        plot.xaxis.major_tick_out = 10
        plot.xgrid.grid_line_color = None
        plot.xaxis.axis_label = "Year"

        if self.lang == "English":
            time_slice1 = BoxAnnotation(left=1810, right=1860, fill_color='#009E73', fill_alpha=0.1)
            plot.add_layout(time_slice1)
            time_slice2 = BoxAnnotation(left=1960, right=2010, fill_color='#009E73', fill_alpha=0.1)
            plot.add_layout(time_slice2)
        elif self.lang == "German":
            time_slice1 = BoxAnnotation(left=1800, right=1899, fill_color='#009E73', fill_alpha=0.1)
            plot.add_layout(time_slice1)
            time_slice2 = BoxAnnotation(left=1946, right=1990, fill_color='#009E73', fill_alpha=0.1)
            plot.add_layout(time_slice2)


        df_hist = pd.read_csv("./historical_events_data/historical_events.csv") 

        for event in df_hist.values:
            historical_event_label = Label(x=event[1], y=event[2], text=event[0],
                                text_align="center", text_baseline="middle",
                                text_font_size="12px", text_font_style="italic",
                                text_color="lightsalmon")
            plot.add_layout(historical_event_label)
        
        medal = plot.circle(x="Year", y="Score", size='Size', level="overlay",
                            fill_color="Color", line_color="Color", fill_alpha=0.5, source=source)
        plot.hover.renderers = [medal]

        plot.text(x="Year", y="Score", x_offset=15, y_offset=-5,  
                text="word", text_align="left", text_baseline="middle",
                text_font_size="12px", text_color='TextColor', source=source)
        
        return plot
