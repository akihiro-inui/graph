import networkx as nx
import matplotlib.pyplot as plt
from utils.file_folder_tool import read_text_file

graph_list = read_text_file('graph_dijkstra.txt')

G = nx.DiGraph()

for line in graph_list:
    # Split nodes and edges
    node = int(line.split('\t')[0])
    edges = line.split('\t')[1:]
    G.add_node(node)
    for edge_info in edges:
        if "," in edge_info:
            edge = int(edge_info.split(',')[0])
            length = int(edge_info.split(',')[1])
            G.add_edge(node, edge, weight=length)


source_node = 1
path_length_dict = {}
for line in graph_list[1:]:
    target_node = int(line.split('\t')[0])
    try:
        length = nx.dijkstra_path_length(G, source_node, target_node)
        path_length_dict[target_node] = length
    except Exception:
        path_length_dict[target_node] = 1000000

target_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

length_dict = {}
for target in target_nodes:
    print(path_length_dict[target])

# Plot graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos)
# nx.draw_networkx_edge_labels(G, pos)
# plt.show()
