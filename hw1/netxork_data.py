import matplotlib.pyplot as plt
import networkx as nx
import random
import functools
import numpy as np
import scipy.sparse
import scipy.sparse.csgraph
import itertools

def main():
	G = nx.Graph()

	#2020
	G.add_node("Georgios Stoupas") 
	G.add_node("Antonis Sidiropoulos")
	G.add_node("Dimitrios Katsaros") 
	G.add_node("Yannis Manolopoulos") 
	#2019
	G.add_node("Dimitrios Papakostas") 
	G.add_node("Leandros Tassiulas") 
	G.add_node("Soheil Eshghi") 
	#
	G.add_node("Pavlos Basaras") 
	G.add_node("George Iosifidis") 
	#
	G.add_node("George Stavropoulos") 
	#
	G.add_node("Payam M. Barnaghi") 
	G.add_node("Georg Gottlob")
	G.add_node("Rahul Pandey") 
	G.add_node("Theodoros Tzouramanis") 
	G.add_node("Athena Vakali") 

	#2018
	G.add_node("Marios Bakratsas")
	#
	G.add_node("Leandros A. Maglaras") 
	G.add_node("Lei Shu") 
	G.add_node("Athanasios Maglaras") 
	G.add_node("Jianmin Jiang") 
	G.add_node("Helge Janicke")
	G.add_node("Tiago J. Cruz")
	#
	G.add_node("Antonia Gogoglou")
	#
	G.add_node("Georgios Sideris")

	#2017
	G.add_node("Ioannis Zozas")
	G.add_node("Stamatia Bibi")
	G.add_node("Panagiotis Bozanis")
	G.add_node("Ioannis Stamelos")

	#2016
	G.add_node("Ioannis-Prodromos Belikaidis")

	#2014
	G.add_node("Alexandra I. Cristea")
	#
	G.add_node("Alexandra Stagkopoulou")
	#
	G.add_node("Muhammad Umer Khan")
	G.add_node("Lars Schmidt-Thieme")
	G.add_node("Alexandros Nanopoulos")
	#
	G.add_node("Katerina Pechlivanidou")	
	#
	G.add_node("Kostas Katsalis")	
	G.add_node("Ioannis Igoumenos")
	G.add_node("Thanasis Korakis")
	#
	G.add_node("Nikos Makris")
	#2013
	G.add_node("Nikos Dimokas")
	#2012
	G.add_node("Alfredo Cuzzocrea")
	G.add_node("Alexis Papadimitriou") 
	#
	G.add_node("Leonidas Akritidis") 
	#
	G.add_node("Stamatia Bibi")
	#
	G.add_node("Donatos Stavropoulos")
	G.add_node("Giannis Kazdaridis")
	#2011
	G.add_node("Vasilis Sourlas")
	G.add_node("Paris Flegkas")
	G.add_node("Georgios S. Paschos")
	#
	G.add_node("Bhaskar Prasad Rimal")
	G.add_node("Admela Jukan")
	G.add_node("Yves Goeleven")
	#
	G.add_node("George Pallis")
	G.add_node("S. Sivasubramanian")
	G.add_node("Athena Vakali")
	#
	G.add_node("Andreas Papadopoulos")

	#2010
	G.add_node("Konstantinos Stamos")
	#2009
	G.add_node("Marios D. Dikaiakos")
	G.add_node("Pankaj Mehra")
	#
	G.add_node("Nicholas Loulloudes")

	#2008
	G.add_node("Ioannis Karydis")
	G.add_node("Apostolos N. Papadopoulos")
	#
	G.add_node("Maria Kontaki")	
	#2007
	G.add_node("Fotis Tsakiridis")
	#2005

	G.add_node("Gökhan Yavas")
	G.add_node("Özgür Ulusoy")

	#2003
	G.add_node("Murat Karakaya")
	#######################################################################3
	#2020
	G.add_edge("Georgios Stoupas","Antonis Sidiropoulos" )
	G.add_edge("Georgios Stoupas","Dimitrios Katsaros" )
	G.add_edge("Georgios Stoupas","Yannis Manolopoulos")
	G.add_edge("Dimitrios Katsaros","Yannis Manolopoulos" )
	G.add_edge("Dimitrios Katsaros","Antonis Sidiropoulos" )
	G.add_edge("Antonis Sidiropoulos","Yannis Manolopoulos" )

	#2019
	G.add_edge("Dimitrios Papakostas","Leandros Tassiulas" )
	G.add_edge("Dimitrios Papakostas","Dimitrios Katsaros" )
	G.add_edge("Dimitrios Papakostas","Soheil Eshghi")
	G.add_edge("Dimitrios Katsaros","Leandros Tassiulas" )
	G.add_edge("Dimitrios Katsaros","Soheil Eshghi" )
	G.add_edge("Leandros Tassiulas","Soheil Eshghi" )
	#
	G.add_edge("Pavlos Basaras","Leandros Tassiulas" )
	G.add_edge("Pavlos Basaras","Dimitrios Katsaros" )
	G.add_edge("Pavlos Basaras","George Iosifidis")
	G.add_edge("Dimitrios Katsaros","George Iosifidis" )
	G.add_edge("Leandros Tassiulas","George Iosifidis" )

	#
	G.add_edge("Dimitrios Katsaros","George Stavropoulos" )
	G.add_edge("Dimitrios Papakostas","George Stavropoulos" )

	#
	G.add_edge("Payam M. Barnaghi","Georg Gottlob" )
	G.add_edge("Payam M. Barnaghi","Dimitrios Katsaros" )
	G.add_edge("Payam M. Barnaghi","Rahul Pandey")
	G.add_edge("Payam M. Barnaghi","Yannis Manolopoulos" )
	G.add_edge("Payam M. Barnaghi","Theodoros Tzouramanis" )
	G.add_edge("Payam M. Barnaghi","Athena Vakali" )
	G.add_edge("Georg Gottlob","Dimitrios Katsaros" )
	G.add_edge("Georg Gottlob","Yannis Manolopoulos" )
	G.add_edge("Georg Gottlob","Rahul Pandey")
	G.add_edge("Georg Gottlob","Athena Vakali" )
	G.add_edge("Georg Gottlob","Theodoros Tzouramanis" )
	G.add_edge("Dimitrios Katsaros","Rahul Pandey" )
	G.add_edge("Dimitrios Katsaros","Theodoros Tzouramanis" )
	G.add_edge("Dimitrios Katsaros","Athena Vakali")
	G.add_edge("Rahul Pandey","Theodoros Tzouramanis" )
	G.add_edge("Rahul Pandey","Athena Vakali")
	G.add_edge("Theodoros Tzouramanis","Athena Vakali")
	#2018
	G.add_edge("Dimitrios Katsaros","Marios Bakratsas" )
	G.add_edge("Marios Bakratsas","Leandros Tassiulas")
	#
	G.add_edge("Leandros A. Maglaras","Lei Shu" )
	G.add_edge("Leandros A. Maglaras","Dimitrios Katsaros" )
	G.add_edge("Leandros A. Maglaras","Athanasios Maglaras" )
	G.add_edge("Leandros A. Maglaras","Jianmin Jiang" )
	G.add_edge("Leandros A. Maglaras","Helge Janicke" )
	G.add_edge("Leandros A. Maglaras","Tiago J. Cruz" )
	G.add_edge("Lei Shu","Athanasios Maglaras" )
	G.add_edge("Lei Shu","Jianmin Jiang" )
	G.add_edge("Lei Shu","Helge Janicke" )
	G.add_edge("Lei Shu","Dimitrios Katsaros" )
	G.add_edge("Lei Shu","Tiago J. Cruz" )
	G.add_edge("Athanasios Maglaras","Jianmin Jiang" )
	G.add_edge("Athanasios Maglaras","Helge Janicke" )
	G.add_edge("Athanasios Maglaras","Dimitrios Katsaros" )
	G.add_edge("Athanasios Maglaras","Tiago J. Cruz" )
	G.add_edge("Jianmin Jiang","Helge Janicke" )
	G.add_edge("Jianmin Jiang","Dimitrios Katsaros" )
	G.add_edge("Jianmin Jiang","Tiago J. Cruz" )
	G.add_edge("Helge Janicke","Dimitrios Katsaros" )
	G.add_edge("Helge Janicke","Tiago J. Cruz" )
	G.add_edge("Dimitrios Katsaros","Tiago J. Cruz" )
	#
	G.add_edge("Antonia Gogoglou","Dimitrios Katsaros" )
	G.add_edge("Antonia Gogoglou","Georgios Stoupas" )
	G.add_edge("Antonia Gogoglou","Antonis Sidiropoulos" )
	G.add_edge("Antonia Gogoglou","Yannis Manolopoulos" )
	#
	G.add_edge("Dimitrios Katsaros","Georgios Sideris" )
	G.add_edge("Georgios Sideris","Yannis Manolopoulos" )
	G.add_edge("Georgios Sideris","Antonis Sidiropoulos" )


	#2017
	G.add_edge("Ioannis Zozas","Stamatia Bibi" )
	G.add_edge("Ioannis Zozas","Dimitrios Katsaros" )
	G.add_edge("Ioannis Zozas","Panagiotis Bozanis" )
	G.add_edge("Ioannis Zozas","Yannis Manolopoulos" )
	G.add_edge("Stamatia Bibi","Dimitrios Katsaros" )
	G.add_edge("Stamatia Bibi","Panagiotis Bozanis" )
	G.add_edge("Stamatia Bibi","Yannis Manolopoulos" )
	G.add_edge("Dimitrios Katsaros","Panagiotis Bozanis" )
	G.add_edge("Dimitrios Katsaros","Yannis Manolopoulos" )
	G.add_edge("Panagiotis Bozanis","Yannis Manolopoulos" )

	G.add_edge("Ioannis Stamelos","Ioannis Stamelos" )
	G.add_edge("Ioannis Stamelos","Panagiotis Bozanis" )
	G.add_edge("Ioannis Stamelos","Dimitrios Katsaros" )
	G.add_edge("Ioannis Stamelos","Stamatia Bibi" )
	G.add_edge("Ioannis Stamelos","Ioannis Zozas" )


	#
	G.add_edge("Georgios Stoupas","Antonis Sidiropoulos")
	G.add_edge("Georgios Stoupas","Antonia Gogoglou")
	G.add_edge("Georgios Stoupas","Yannis Manolopoulos")

	#2016
	G.add_edge("Marios Bakratsas","Pavlos Basaras")
	G.add_edge("Pavlos Basaras","Leandros Tassiulas")
	#
	G.add_edge("Dimitrios Papakostas","Pavlos Basaras")
	G.add_edge("Leandros Tassiulas","Dimitrios Papakostas")

	#
	G.add_edge("Pavlos Basaras","Leandros A. Maglaras")
	G.add_edge("Pavlos Basaras","Ioannis-Prodromos Belikaidis")
	G.add_edge("Ioannis-Prodromos Belikaidis","Leandros A. Maglaras")
	G.add_edge("Ioannis-Prodromos Belikaidis","Dimitrios Katsaros")

	#2015
	G.add_edge("Pavlos Basaras","Helge Janicke")
	#2014
	G.add_edge("Alexandra I. Cristea", "Dimitrios Katsaros")
	G.add_edge("Alexandra I. Cristea", "Yannis Manolopoulos")
	#
	G.add_edge("Alexandra Stagkopoulou", "Pavlos Basaras")
	G.add_edge("Alexandra Stagkopoulou", "Dimitrios Katsaros")
	#
	G.add_edge("Pavlos Basaras","Muhammad Umer Khan")
	G.add_edge("Muhammad Umer Khan","Lars Schmidt-Thieme")
	G.add_edge("Muhammad Umer Khan","Alexandros Nanopoulos")
	G.add_edge("Muhammad Umer Khan","Dimitrios Katsaros")
	G.add_edge("Pavlos Basaras","Lars Schmidt-Thieme")
	G.add_edge("Pavlos Basaras","Alexandros Nanopoulos")
	G.add_edge("Lars Schmidt-Thieme","Alexandros Nanopoulos")
	G.add_edge("Lars Schmidt-Thieme","Dimitrios Katsaros")
	G.add_edge("Alexandros Nanopoulos","Dimitrios Katsaros")
	#
	G.add_edge("Katerina Pechlivanidou","Leandros Tassiulas")
	G.add_edge("Katerina Pechlivanidou","Dimitrios Katsaros")
	G.add_edge("Leandros Tassiulas","Dimitrios Katsaros")
	#
	G.add_edge("Katerina Pechlivanidou","Kostas Katsalis")
	G.add_edge("Katerina Pechlivanidou","Ioannis Igoumenos")
	G.add_edge("Katerina Pechlivanidou","Thanasis Korakis")
	G.add_edge("Kostas Katsalis","Dimitrios Katsaros")
	G.add_edge("Kostas Katsalis","Ioannis Igoumenos")
	G.add_edge("Kostas Katsalis","Thanasis Korakis")
	G.add_edge("Kostas Katsalis","Leandros Tassiulas")
	G.add_edge("Ioannis Igoumenos","Dimitrios Katsaros")
	G.add_edge("Ioannis Igoumenos","Thanasis Korakis")
	G.add_edge("Ioannis Igoumenos","Leandros Tassiulas")
	G.add_edge("Dimitrios Katsaros","Thanasis Korakis")
	G.add_edge("Thanasis Korakis","Leandros Tassiulas")
	#
	G.add_edge("Nikos Makris","Dimitrios Katsaros")
	G.add_edge("Nikos Makris","Thanasis Korakis")
	G.add_edge("Nikos Makris","Leandros Tassiulas")
	#2013
	G.add_edge("Nikos Dimokas", "Dimitrios Katsaros")
	#
	G.add_edge("Pavlos Basaras", "Leandros A. Maglaras")

	#2012
	G.add_edge("Alfredo Cuzzocrea","Alexis Papadimitriou")
	G.add_edge("Alfredo Cuzzocrea","Dimitrios Katsaros")
	G.add_edge("Alfredo Cuzzocrea","Yannis Manolopoulos")
	G.add_edge("Alexis Papadimitriou","Dimitrios Katsaros")
	G.add_edge("Alexis Papadimitriou","Yannis Manolopoulos")
	#
	G.add_edge("Leonidas Akritidis","Dimitrios Katsaros")
	G.add_edge("Leonidas Akritidis","Panagiotis Bozanis")
	#
	G.add_edge("Stamatia Bibi","Dimitrios Katsaros")
	G.add_edge("Stamatia Bibi","Panagiotis Bozanis")
	#
	G.add_edge("Donatos Stavropoulos","Giannis Kazdaridis")
	G.add_edge("Donatos Stavropoulos","Thanasis Korakis")
	G.add_edge("Donatos Stavropoulos","Dimitrios Katsaros")
	G.add_edge("Donatos Stavropoulos","Leandros Tassiulas")
	G.add_edge("Giannis Kazdaridis","Thanasis Korakis")
	G.add_edge("Giannis Kazdaridis","Dimitrios Katsaros")
	G.add_edge("Giannis Kazdaridis","Leandros Tassiulas")
	#2011
	G.add_edge("Vasilis Sourlas","Paris Flegkas")
	G.add_edge("Vasilis Sourlas","Georgios S. Paschos")
	G.add_edge("Vasilis Sourlas","Dimitrios Katsaros")
	G.add_edge("Vasilis Sourlas","Leandros Tassiulas")
	G.add_edge("Paris Flegkas","Georgios S. Paschos")
	G.add_edge("Paris Flegkas","Dimitrios Katsaros")
	G.add_edge("Paris Flegkas","Leandros Tassiulas")
	G.add_edge("Georgios S. Paschos","Dimitrios Katsaros")
	G.add_edge("Georgios S. Paschos","Leandros Tassiulas")
	#
	G.add_edge("Bhaskar Prasad Rimal","Admela Jukan")
	G.add_edge("Bhaskar Prasad Rimal","Dimitrios Katsaros")
	G.add_edge("Bhaskar Prasad Rimal","Yves Goeleven")
	G.add_edge("Admela Jukan","Dimitrios Katsaros")
	G.add_edge("Admela Jukan","Yves Goeleven")
	G.add_edge("Dimitrios Katsaros","Yves Goeleven")
	#
	G.add_edge("Dimitrios Katsaros","George Pallis")
	G.add_edge("Dimitrios Katsaros","S. Sivasubramanian")
	G.add_edge("Dimitrios Katsaros","Athena Vakali")
	G.add_edge("George Pallis","S. Sivasubramanian")
	G.add_edge("George Pallis","Athena Vakali")
	G.add_edge("S. Sivasubramanian","Athena Vakali")
	#
	G.add_edge("Nikos Dimokas","Leandros Tassiulas")
	G.add_edge("Nikos Dimokas","Yannis Manolopoulos")
	#
	G.add_edge("Andreas Papadopoulos","Dimitrios Katsaros")


	#2010
	G.add_edge("Konstantinos Stamos","George Pallis")
	G.add_edge("Konstantinos Stamos","Athena Vakali")
	G.add_edge("Konstantinos Stamos","Dimitrios Katsaros")
	G.add_edge("Konstantinos Stamos","Antonis Sidiropoulos")
	G.add_edge("Konstantinos Stamos","Yannis Manolopoulos")
	G.add_edge("George Pallis","Athena Vakali")
	G.add_edge("George Pallis","Antonis Sidiropoulos")
	G.add_edge("George Pallis","Yannis Manolopoulos")
	G.add_edge("Athena Vakali","Antonis Sidiropoulos")
	G.add_edge("Athena Vakali","Yannis Manolopoulos")

	#2009
	G.add_edge("Marios D. Dikaiakos","Dimitrios Katsaros")
	G.add_edge("Marios D. Dikaiakos","Pankaj Mehra")
	G.add_edge("Marios D. Dikaiakos","George Pallis")
	G.add_edge("Marios D. Dikaiakos","Athena Vakali")
	G.add_edge("Pankaj Mehra","George Pallis")
	G.add_edge("Pankaj Mehra","Athena Vakali")
	G.add_edge("Pankaj Mehra","Dimitrios Katsaros")
	#
	G.add_edge("Nicholas Loulloudes","George Pallis")
	G.add_edge("Nicholas Loulloudes","Dimitrios Katsaros")
	G.add_edge("Nicholas Loulloudes","Marios D. Dikaiakos")
	G.add_edge("Nicholas Loulloudes","Nicholas Loulloudes")
	G.add_edge("Nicholas Loulloudes","Leandros Tassiulas")
	G.add_edge("Leandros Tassiulas","George Pallis")
	G.add_edge("Leandros Tassiulas","Marios D. Dikaiakos")
	#
	G.add_edge("Alfredo Cuzzocrea","Dimitrios Katsaros")
	G.add_edge("Alfredo Cuzzocrea","Yannis Manolopoulos")
	G.add_edge("Alfredo Cuzzocrea","Alexis Papadimitriou")

	#2008
	G.add_edge("Ioannis Karydis","Alexandros Nanopoulos")
	G.add_edge("Ioannis Karydis","Apostolos N. Papadopoulos")
	G.add_edge("Ioannis Karydis","Dimitrios Katsaros")
	G.add_edge("Ioannis Karydis","Yannis Manolopoulos")

	G.add_edge("Alexandros Nanopoulos","Apostolos N. Papadopoulos")
	G.add_edge("Alexandros Nanopoulos","Yannis Manolopoulos")
	G.add_edge("Dimitrios Katsaros","Apostolos N. Papadopoulos")
	G.add_edge("Yannis Manolopoulos","Apostolos N. Papadopoulos")
		
	#
	G.add_edge("Alexandros Nanopoulos","Apostolos N. Papadopoulos")
	G.add_edge("Alexandros Nanopoulos","Yannis Manolopoulos")
	G.add_edge("Dimitrios Katsaros","Apostolos N. Papadopoulos")
	G.add_edge("Yannis Manolopoulos","Apostolos N. Papadopoulos")

	#
	G.add_edge("Maria Kontaki","Dimitrios Katsaros")
	G.add_edge("Maria Kontaki","Yannis Manolopoulos")

	#2007
	G.add_edge("Fotis Tsakiridis","Panagiotis Bozanis")
	G.add_edge("Fotis Tsakiridis","Dimitrios Katsaros")

	#2005
	G.add_edge("Gökhan Yavas","Dimitrios Katsaros")
	G.add_edge("Gökhan Yavas","Özgür Ulusoy")
	G.add_edge("Gökhan Yavas","Yannis Manolopoulos")
	G.add_edge("Dimitrios Katsaros","Özgür Ulusoy")
	G.add_edge("Özgür Ulusoy","Yannis Manolopoulos")
	#2003
	G.add_edge("Murat Karakaya","Dimitrios Katsaros")
	G.add_edge("Murat Karakaya","Alexandros Nanopoulos")
	G.add_edge("Murat Karakaya","Gökhan Yavas")
	G.add_edge("Murat Karakaya","Özgür Ulusoy")
	G.add_edge("Murat Karakaya","Yannis Manolopoulos")	
	G.add_edge("Özgür Ulusoy","Alexandros Nanopoulos")
	G.add_edge("Gökhan Yavas","Alexandros Nanopoulos")

	#########################################################################
	print(G.number_of_nodes())

	print(G.number_of_edges())
	#print(list(G.nodes))
	#list(G.edges))
	nx.draw(G, with_labels = False)
	plt.savefig("no_names_graph.png")
	#nx.draw(G, with_labels = True)
	#plt.savefig("names_graph.png")
	
	
	print("Local clustering coefficient for each node : ")
	c=nx.clustering(G)
	print(c) 
	for key, value in c.items():
    		print(key, '	: ', value)
	print("Clustering coefficient as average of lcc: ")
	cc_a = nx.average_clustering(G)
	print(cc_a)
	print("Clustering coefficient as network transitivity : ")
	cc_t = nx.transitivity(G)
	print(cc_t)
	print("Characteristic Path Length of graph : ")
	l = nx.average_shortest_path_length(G)
	print(l)
	print("------------degree_centrality---------------")
	
	d=nx.degree_centrality(G)
	for key, value in d.items():
    		print(key, '	: ', value)
	cc = nx.closeness_centrality(G)
	print("------------closeness_centrality---------------")
	
	
	for key, value in cc.items():
    		print(key, '	: ', value)
	bc =nx.betweenness_centrality(G)
	print("-------------betweenness_centrality------------")
	
	for key, value in bc.items():
    		print(key, '	: ', value)


if __name__ == "__main__":
    main()

