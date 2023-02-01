# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
# rm after TEST 
from string import ascii_lowercase as lowercase
import gzip
import pandas as pd
import re
import glob
from .visu_utils import normalize_scores

# TODO big refacto to clean the code (should look like a real python class)

class TreeGraph():

    g = nx.Graph()

    list_files = glob.glob("./model_outputs/" + "*.csv")
    [print(f) for f in list_files]
    
    for f in list_files: 
        df = pd.read_csv(f, sep=",", encoding='utf-8')  # TODO check that it doesnt switch to ; instead of , when generated files
        df.rename(columns={f'AP All':'Score'}, inplace=True)  # TODO change to the right column 
        print(df['Score'].array)
        df = normalize_scores(df)  # TODO not sure it's really useful in this case 

        # To retrieve the time slice  TODO idk how to include this scale into the rendering 
        time_slice = re.findall("\d+-\d+",df.columns[1])[0] 
        start, end = time_slice.split("-")
        mean_year = str(round((int(start)+int(end))/2))
        df['Year'] = mean_year
        print(df["Year"].values)

        idx = 0
        for i in df['Parent'].values:
            word1, word2 = re.split(",", i)
            tup = (word1, word2)
            src_word = df["word"][idx]
            print(src_word)
            score = df["Score"][idx] 
            print("SCORE", score) 
            
            # add the src word into the graph 
            g.add_node(src_word)
            # add the related words
            if word1 != "None":
                # TODO indicate the level on the tree, rn they're all linked to the same "awful" 
                # TODO modulate the distances between the nodes using the 'Score' value  
                g.add_edge(word1, src_word)  #, word=src_word
            if word2 != "None":
                g.add_edge(src_word, word2)
            idx+=1
            g._node[src_word]['word'] = src_word
            g._node[src_word]['score'] = score

        """
        for v in g:
            print(v)
            g._node[v]['word'] = str(v)
            g._node[v]['score'] = score  # TODO that can work since we're going to indice the vertices ? 

        """

    #nx.draw(g, with_labels = True)
    #plt.savefig("./filename3.png")



"""
Dummy
"""

"""
def generate_graph(words):
    G = nx.Graph(name="words")
    lookup = {c: lowercase.index(c) for c in lowercase}

    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i + 1 :]
            j = lookup[c]  # lowercase.index(c)
            for cc in lowercase[j + 1 :]:
                yield left + cc + right

    candgen = (
        (word, cand)
        for word in sorted(words)
        for cand in edit_distance_one(word)
        if cand in words
    )
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph():
    #Return the words example graph from the Stanford GraphBase
    fh = gzip.open("./words_dat.txt.gz", "r")
    words = set()
    for line in fh.readlines():
        line = line.decode()
        print("LINE", line)
        if line.startswith("*"):
            continue
        w = str(line[0:5])
        words.add(w)
    return generate_graph(words)


G = words_graph()
print("Loaded words_dat.txt containing 5757 five-letter English words.")
print("Two words are connected if they differ in one letter.")
print(G)
print(f"{nx.number_connected_components(G)} connected components")

for (source, target) in [("chaos", "order"), ("nodes", "graph"), ("pound", "marks")]:
    print(f"Shortest path between {source} and {target} is")
    try:
        shortest_path = nx.shortest_path(G, source, target)
        for n in shortest_path:
            print(n)
    except nx.NetworkXNoPath:
        print("None")


# draw a subset of the graph
boundary = list(nx.node_boundary(G, shortest_path))
G.add_nodes_from(shortest_path, color="red")
G.add_nodes_from(boundary, color="blue")
H = G.subgraph(shortest_path + boundary)
colors = nx.get_node_attributes(H, "color")
options = {"node_size": 1500, "alpha": 0.3, "node_color": colors.values()}
pos = nx.kamada_kawai_layout(H) # TODO needed for the labels 
nx.draw(H, pos, **options) # pos
nx.draw_networkx_labels(H, pos, font_weight="bold")  # TODO include draw_networkx_labels and pos to help print the labels 
plt.show()
"""