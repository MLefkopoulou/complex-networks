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




def draw_graph3(networkx_graph,notebook=True,output_filename='graph.html',show_buttons=False,only_physics_buttons=False):
        """
        This function accepts a networkx graph object,
        converts it to a pyvis network object preserving its node and edge attributes,
        and both returns and saves a dynamic network visualization.

        Valid node attributes include:
            "size", "value", "title", "x", "y", "label", "color".

            (For more info: https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node)

        Valid edge attributes include:
            "arrowStrikethrough", "hidden", "physics", "title", "value", "width"

            (For more info: https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_edge)


        Args:
            networkx_graph: The graph to convert and display
            notebook: Display in Jupyter?
            output_filename: Where to save the converted network
            show_buttons: Show buttons in saved version of network?
            only_physics_buttons: Show only buttons controlling physics of network?
        """

        

        # make a pyvis network
        pyvis_graph = net.Network(notebook=notebook)
        pyvis_graph.width = '1000px'
        # for each node and its attributes in the networkx graph
        for node,node_attrs in networkx_graph.nodes(data=True):
            pyvis_graph.add_node(node,**node_attrs)
    	#         print(node,node_attrs)

        # for each edge and its attributes in the networkx graph
        for source,target,edge_attrs in networkx_graph.edges(data=True):
            # if value/width not specified directly, and weight is specified, set 'value' to 'weight'
            if not 'value' in edge_attrs and not 'width' in edge_attrs and 'weight' in edge_attrs:
                # place at key 'value' the weight of the edge
                edge_attrs['value']=edge_attrs['weight']
                
            if (buttons == true):
            	pyvis_graph.show_buttons(filter_=["edges"])
            # add the edge
            pyvis_graph.add_edge(source,target,arrowStrikethrough= False)

        # turn buttons on
        if show_buttons:
            if only_physics_buttons:
                pyvis_graph.show_buttons(filter_=['physics'])
            else:
                pyvis_graph.show_buttons()

        # return and also save
        return pyvis_graph.show(output_filename)




def main():

	with open('DimitriosKatsaros.bib') as bibtex_file:
	    bib_database = bibtexparser.load(bibtex_file)

	DG = nx.DiGraph()
	last= 0
	author_node = []
	print(len(bib_database.entries))
	for x in range(len(bib_database.entries)):
		last = 0
		author_node = []
		entry_keys = set(bib_database.entries[x].keys())
		if('author' in entry_keys):
			li = bib_database.entries[x]['author'].splitlines()
			for y in li:
				if(last != len(li)-1):
					y = y[:-4]
				print (y)
				author_node.append(y)
				last = last +1
			print (author_node)
			for new_author in author_node :
				if new_author not in DG:
					DG.add_node(new_author)
			for from_node in range(len(author_node)):
				for to_node in range(from_node+1,len(author_node)):	
					if(DG.has_edge(author_node[from_node],author_node[to_node]) == False):
						print("adding")
						DG.add_edge(author_node[from_node],author_node[to_node])
					else:
						print("no")
					
					
					
					
					
					
					
					
					
					
					
					
					
					
	print(DG.number_of_edges())				
	print(DG.number_of_nodes())

	nx.spring_layout(DG,k=0.95,iterations=20)
	nx.draw(DG, with_labels = True)
	plt.savefig("ask4_no_names_graph.png")

	pr = nx.pagerank(DG,alpha = 0.85)
	for key, value in pr.items():
    		print(key, '	: ', value)
	#draw_graph3(DG,output_filename='graph_output.html', notebook=False)

if __name__ == "__main__":
    main()

