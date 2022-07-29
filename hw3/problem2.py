import bibtexparser
import matplotlib.pyplot as plt
import networkx as nx
import random
import functools
import numpy as np
import scipy.sparse
import scipy.sparse.csgraph
import itertools
from networkx import Graph
from pyvis import network as net
from networkx.drawing.nx_agraph import to_agraph 
import subprocess
def main():

	with open('DimitriosKatsaros.bib') as bibtex_file:
	    bib_database = bibtexparser.load(bibtex_file)

	G = nx.Graph()
	last= 0
	author_node = []
	#print(len(bib_database.entries))
	for x in range(len(bib_database.entries)):
		last = 0
		author_node = []
		entry_keys = set(bib_database.entries[x].keys())
		if('author' in entry_keys):
			li = bib_database.entries[x]['author'].splitlines()
			for y in li:
				if(last != len(li)-1):
					y = y[:-4]
					y = y.replace(" ", "_")
				#print (y)
				author_node.append(y)
				last = last +1
			#print (author_node)
			for new_author in author_node :
				if new_author not in G:
					G.add_node(new_author)
			for from_node in range(len(author_node)):
				for to_node in range(from_node+1,len(author_node)):	
					if(G.has_edge(author_node[from_node],author_node[to_node]) == False):
						print(author_node[from_node]+" "+author_node[to_node])
						G.add_edge(author_node[from_node],author_node[to_node])
					
					
			
					
	print(G.number_of_edges())				
	print(G.number_of_nodes())

	nx.spring_layout(G,k=0.95,iterations=20)
	nx.draw(G, with_labels = True)
	plt.savefig("p2.png")

        subprocess.call(['java', '-jar', 'AviNet.jar'])

if __name__ == "__main__":
    main()
