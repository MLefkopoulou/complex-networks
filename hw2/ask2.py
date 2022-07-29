import matplotlib.pyplot as plt
import networkx as nx
import random
import functools
import numpy as np
import scipy.sparse
import scipy.sparse.csgraph
import itertools

G = nx.Graph()
G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")
G.add_edge("1","4")
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("3","4")
G.add_edge("3","5")
G.add_edge("2","5")
G.add_edge("4","5")


print("Shortest pths from node 1 : ")
print([p for p in nx.all_shortest_paths(G, source="1", target="1")])
print([p for p in nx.all_shortest_paths(G, source="1", target="2")])
print([p for p in nx.all_shortest_paths(G, source="1", target="3")])
print([p for p in nx.all_shortest_paths(G, source="1", target="4")])
print([p for p in nx.all_shortest_paths(G, source="1", target="5")])
print("Shortest pths from node 2 : ")
print([p for p in nx.all_shortest_paths(G, source="2", target="1")])
print([p for p in nx.all_shortest_paths(G, source="2", target="2")])
print([p for p in nx.all_shortest_paths(G, source="2", target="3")])
print([p for p in nx.all_shortest_paths(G, source="2", target="4")])
print([p for p in nx.all_shortest_paths(G, source="2", target="5")])
print("Shortest pths from node 3 : ")
print([p for p in nx.all_shortest_paths(G, source="3", target="1")])
print([p for p in nx.all_shortest_paths(G, source="3", target="2")])
print([p for p in nx.all_shortest_paths(G, source="3", target="3")])
print([p for p in nx.all_shortest_paths(G, source="3", target="4")])
print([p for p in nx.all_shortest_paths(G, source="3", target="5")])
print("Shortest pths from node 4 : ")
print([p for p in nx.all_shortest_paths(G, source="4", target="1")])
print([p for p in nx.all_shortest_paths(G, source="4", target="2")])
print([p for p in nx.all_shortest_paths(G, source="4", target="3")])
print([p for p in nx.all_shortest_paths(G, source="4", target="4")])
print([p for p in nx.all_shortest_paths(G, source="4", target="5")])
print("Shortest pths from node 5 : ")
print([p for p in nx.all_shortest_paths(G, source="5", target="1")])
print([p for p in nx.all_shortest_paths(G, source="5", target="2")])
print([p for p in nx.all_shortest_paths(G, source="5", target="3")])
print([p for p in nx.all_shortest_paths(G, source="5", target="4")])
print([p for p in nx.all_shortest_paths(G, source="5", target="5")])



print(nx.edge_betweenness_centrality(G,k=5,normalized = False))
