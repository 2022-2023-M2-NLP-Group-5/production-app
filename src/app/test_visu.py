import random
from random import randint
from bokeh.models import (Arrow, ColumnDataSource, CustomJS, Label,
                          NormalHead, SingleIntervalTicker, TapTool)
from bokeh.plotting import figure, show
from bokeh.sampledata.sprint import sprint
import pandas as pd


fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }
line_color = { "gold": "#c8a850", "silver": "#b0b0b1", "bronze": "#98715d" }

def selected_name(name, medal, year):
    return name if medal == "gold" and year in [1988, 1968, 1936, 1896] else ""

t0 = sprint.Time[0]

sprint["Abbrev"]       = sprint.Country
sprint["Medal"]        = sprint.Medal.map(lambda medal: medal.lower())
sprint["Speed"]        = 100.0/sprint.Time
sprint["MetersBack"]   = 100.0*(1.0 - t0/sprint.Time)
sprint["MedalFill"]    = sprint.Medal.map(lambda medal: fill_color[medal])
sprint["MedalLine"]    = sprint.Medal.map(lambda medal: line_color[medal])
sprint["SelectedName"] = sprint[["Name", "Medal", "Year"]].apply(tuple, axis=1).map(lambda args: selected_name(*args))

def map_names(data):
    words =  ["awful", "solemn", "majestic", "awe", "dread", "pensive", "gloomy", "horrible", "appalling", "awful", "terrible", "awful", "wonderful", "awful", "weird"]
    #new_df = pd.DataFrame()
    for i in data["Name"]: 
        #i = random.choice(words)
        #data.at[i.iat, "Name"] = random.choice(words)
        data = data.replace([i],random.choice(words))
    for j in data["Time"]: 
        #data.at[j, "Time"] = str(randint(50, 100))+"%"
        data = data.replace([j], str(randint(50, 100))+"%")
    print(data)
    return data


class Clusters_Visualization2():
    #def __init__(self, data):
    #    self.source = ColumnDataSource(data)

    data = sprint
    data = map_names(data)

    source = ColumnDataSource(data)



    tooltips = """
    <div>
        <span style="font-size: 15px;">@Name</span>&nbsp;
    </div>
    <div>
        <span style="font-size: 17px; font-weight: bold;">@Time</span>&nbsp;
    </div>
    """

    # {0.00}

    plot = figure(width=1000, height=700, x_range=(sprint.MetersBack.max()+2, 0),
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

    plot.yaxis.ticker = [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020] #[1900, 1912, 1924, 1936, 1952, 1964, 1976, 1988, 2000, 2012]
    plot.yaxis.major_tick_in = -5
    plot.yaxis.major_tick_out = 10
    plot.ygrid.grid_line_color = None

    medal = plot.circle(x="MetersBack", y="Year", size=10, source=source, level="overlay",
                        fill_color="MedalFill", line_color="MedalLine", fill_alpha=0.5)
    plot.hover.renderers = [medal]

    plot.text(x="MetersBack", y="Year", x_offset=10, y_offset=-5,
            text="SelectedName", text_align="left", text_baseline="middle",
            text_font_size="12px", source=source)

