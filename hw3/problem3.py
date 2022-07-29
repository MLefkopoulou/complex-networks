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
	value_node = 1;
	dictionary = {};
	distances ={};
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
					y = y.replace(' ', '_')
					
				else:
					y = y.replace(' ', '_')
				author_node.append(y)
				last = last +1
				if(y not in dictionary):
					dictionary.update({y: value_node})
					value_node = value_node+1;
			#print (author_node)
		
			for new_author in author_node :
				new_node = dictionary.get(new_author)
				if new_node not in G:
					G.add_node(new_node)
			for from_node in range(len(author_node)):
				for to_node in range(from_node+1,len(author_node)):
					from_new_node =dictionary.get(author_node[from_node])
					to_new_node = dictionary.get(author_node[to_node])
					if(G.has_edge(from_new_node,to_new_node) == False):
						print(str(from_new_node)+" "+str(to_new_node))
						G.add_edge(from_new_node,to_new_node)
									
			
					
	print(G.number_of_edges())				
	print(G.number_of_nodes())
	pos = nx.random_layout(G)
	x=1;
	value_node = 1;
	for x in range(len(pos)):
		print_s = str(pos.get(x)).replace("[","")
		print_s =print_s.replace("]","")
		splited = print_s.split(sep = " ")
		papaki = "@"
		first= 0
		
		for x in splited:
			print_s = str(x).replace(" ","")
			if(len(print_s) != 0) : 
				if(first == 0):
					if(x!='None'):
						papaki = papaki+str(int(float(x)*1000))+","
						first = first+1
				else :
					papaki = papaki+str(int(float(x)*1000))
		print(papaki)
		distances.update({value_node: papaki})
		value_node = value_node+1
	print("distances")
	for k in range(len(pos)):
		print(str(distances.get(k)))
		
	for line in nx.generate_adjlist(G):
		nodes_s = line.split(sep = " ")
		ax = ""
		times = 1;
		for x in nodes_s:
			
			if(times == 1):

				ax = ax+str(x)+"	"+str(list(distances.values())[int(x)-1])+"	"
				times = times+1
			else:
				ax = ax+str(x)+"	"
		print(ax)
		
	
	#	nd = 1;
	#	print_string = ""
	#	for spl in nodes_s:
	#		if(nd == 1):
	#			print_string = str(spl) +"\t"+ str(distances.get(spl))
	#			nd = nd+1
	#		else:
	#			print_string = str(spl)+"\t"
	#	print(print_string)
	for node_x in range(len(dictionary)):
		print(str(list(dictionary)[node_x])+"---"+str(list(dictionary.values())[node_x]))
if __name__ == "__main__":
    main()
