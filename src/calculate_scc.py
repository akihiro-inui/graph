import networkx as nx
from utils.file_folder_tool import read_text_file

graph_list = read_text_file('junk/directed_graph.txt')

G = nx.DiGraph()

for line in graph_list:
    # Split nodes and edges
    node = int(line.split(' ')[0])
    edge = int(line.split(' ')[1])
    G.add_node(node)
    G.add_edge(node, edge)

# Compute SCC
scc = nx.strongly_connected_components(G)
sorted_result = [len(c) for c in sorted(scc, key=len, reverse=True)]