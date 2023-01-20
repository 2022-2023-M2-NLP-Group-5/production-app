import networkx as nx
from bokeh.models import Circle, MultiLine
from bokeh.plotting import figure, from_networkx
from .tree_graph import TreeGraph

# TODO big refacto to clean the code (should look like a real python class)

class TreeVisu():
    G = TreeGraph().g #nx.karate_club_graph()

    SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "darkgrey", "red"

    edge_attrs = {}
    for start_node, end_node, _ in G.edges(data=True):
        edge_color = SAME_CLUB_COLOR
        edge_attrs[(start_node, end_node)] = edge_color

    nx.set_edge_attributes(G, edge_attrs, "darkgray") 

    plot = figure(width=600, height=600, #x_range=(-2, 2), #y_range=(1880, 2020), TODO adjust the values of the nodes 
                x_axis_location="below", y_axis_location="left", toolbar_location="right",
                title="Tree View", tooltips="Word: @word, Shift score: @score") 
    plot.grid.grid_line_color = None


    graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
    graph_renderer.node_renderer.glyph = Circle(y="Year", x="score", size=15, fill_color="mediumaquamarine")
    graph_renderer.edge_renderer.glyph = MultiLine(line_color="darkgray", 
                                                line_alpha=0.8, line_width=1.5)
    plot.renderers.append(graph_renderer)

    plot.yaxis.ticker = [1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020]
    plot.yaxis.major_tick_in = -5
    plot.yaxis.major_tick_out = 10
    plot.ygrid.grid_line_color = None
    plot.yaxis.axis_label = "Year"
