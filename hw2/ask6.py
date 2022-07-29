import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

from networkx.drawing.nx_agraph import to_agraph 
DG = nx.DiGraph()
DG.add_node("1")
DG.add_node("2")
DG.add_node("3")
DG.add_node("4")
DG.add_node("5")


DG.add_edge("1","1")
DG.add_edge("1","2")
DG.add_edge("3","1")
DG.add_edge("2","3")
DG.add_edge("3","2")
DG.add_edge("3","4")
DG.add_edge("4","3")
DG.add_edge("4","5")
DG.add_edge("5","4")
print("Number of nodes : "+ str(DG.number_of_nodes()))

print("Number of edges : "+ str(DG.number_of_edges()))


pr = nx.pagerank(DG, alpha=0.1)

print("Page rank for d = 0.1 : ")
for key, value in sorted(pr.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
print("\n")
pr = nx.pagerank(DG, alpha= 0.3)
print("Page rank for d = 0.3 : ")
for key, value in sorted(pr.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
print("\n")
pr = nx.pagerank(DG, alpha=0.5)
print("Page rank for d = 0.5 : ")
for key, value in sorted(pr.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
print("\n")
pr = nx.pagerank(DG, alpha=0.85)
print("Page rank for d = 0.85 : ")
for key, value in sorted(pr.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
print("\n")
A = to_agraph(DG) 
A.layout('dot')                                                                 
A.draw('pagerank.png') 

