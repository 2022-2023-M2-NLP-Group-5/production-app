# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

# TODO big refacto to clean the code (should look like a real python class)


class TreeGraph():
    g = nx.Graph()

    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 5)

    nx.draw(g, with_labels = True)
    #plt.savefig("./filename.png")