import networkx as nx
from utils.file_folder_tool import read_text_file

graph_list = read_text_file('junk/graph.txt')

G = nx.Graph()

for line in graph_list:
    # Split nodes and edges
    node = int(line.split('\t')[0])
    edges = line.split('\t')[1:]
    G.add_node(node)
    for edge in edges:
        if edge != "":
            try:
                G.add_edge(node, int(edge))
            except Exception:
                print("Error while adding edges")

#print(len(nx.minimum_node_cut(G)))
bw_dict = nx.betweenness_centrality(G)
print({k: v for k, v in sorted(bw_dict.items(), key=lambda item: item[1], reverse=True)})