import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import json

stations = json.loads(open("stations.json").read())
np.random.seed(69)

graph = nx.Graph()
graph.add_nodes_from([x["name"] for x in stations])
for s in stations:
    for c in s["connections"]:
        graph.add_edge(s["name"], c)

plt.figure(figsize=(12,12), dpi=500)
nx.draw(graph, with_labels=True ,node_color="green", node_size=50, edge_color="red", font_size=6, font_weight="bold")
plt.savefig("network_labels.png")
# plt.clf()
# nx.draw(graph, node_color="green", node_size=50, edge_color="red", font_size=6, font_weight="bold")
# plt.savefig("network_nolabels.png")