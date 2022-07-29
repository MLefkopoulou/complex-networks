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



#calculation of SPBC






p11 =  list(nx.all_shortest_paths(G, source="1", target="1"))
p12 =  list(nx.all_shortest_paths(G, source="1", target="2"))
p13 =  list(nx.all_shortest_paths(G, source="1", target="3"))
p14 =  list(nx.all_shortest_paths(G, source="1", target="4"))
p15 =  list(nx.all_shortest_paths(G, source="1", target="5"))

p21 =  list(nx.all_shortest_paths(G, source="2", target="1"))
p22 =  list( nx.all_shortest_paths(G, source="2", target="2"))
p23 =  list( nx.all_shortest_paths(G, source="2", target="3"))
p24 =  list( nx.all_shortest_paths(G, source="2", target="4"))
p25 =  list( nx.all_shortest_paths(G, source="2", target="5"))

p31 =   list(nx.all_shortest_paths(G, source="3", target="1"))
p32 =  list(nx.all_shortest_paths(G, source="3", target="2"))
p33 =  list(nx.all_shortest_paths(G, source="3", target="3"))
p34 = list( nx.all_shortest_paths(G, source="3", target="4"))
p35 = list( nx.all_shortest_paths(G, source="3", target="5"))

p41 = list( nx.all_shortest_paths(G, source="4", target="1"))
p42 =  list( nx.all_shortest_paths(G, source="4", target="2"))
p43 =  list( nx.all_shortest_paths(G, source="4", target="3"))
p44 =  list( nx.all_shortest_paths(G, source="4", target="4"))
p45 =  list(nx.all_shortest_paths(G, source="4", target="5"))

p51 = list( nx.all_shortest_paths(G, source="5", target="1"))
p52 =  list(nx.all_shortest_paths(G, source="5", target="2"))
p53 =  list(nx.all_shortest_paths(G, source="5", target="3"))
p54 =  list(nx.all_shortest_paths(G, source="5", target="4"))
p55 = list(nx.all_shortest_paths(G, source="5", target="5"))
all = 0;
cb = 0

for path in p12:
	times = 0;
	if "1" in path : 
		times =times+1
		
cb = cb+ times / len(p12)

for path in p13:
	times = 0;
	if "1" in path : 
		times =times+1

cb = cb + times / len(p13)
for path in p14:
	times = 0;
	if "1" in path : 
		times =times+1

cb = cb+ times / len(p14)
for path in p15:
	times = 0;
	if "1" in path : 
		times =times+1

cb = cb+ times / len(p15)


for path in p23:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p23))
cb = cb + times / len(p23)


for path in p24:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p24))
cb = cb + times / len(p24)
for path in p25:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p25))
cb = cb + times / len(p25)

for path in p32:
	times = 0;
	if "1" in path : 
		times =times+1
		
print(times / len(p32))		
cb = cb + times / len(p32)
for path in p34:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p34))
cb = cb + times / len(p34)
for path in p35:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p35))
cb = cb + times / len(p35)
for path in p42:
	times = 0;
	if "1" in path : 
		times =times+1
cb = cb + times / len(p42)
for path in p43:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p43))
cb = cb + times / len(p43)

for path in p45:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p43))
cb = cb + times / len(p45)
for path in p52:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p52))
cb = cb + times / len(p52)
for path in p53:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p53))
cb = cb + times / len(p53)
for path in p54:
	times = 0;
	if "1" in path : 
		times =times+1
print(times / len(p54))
cb = cb + times / len(p54)


print("1--------> "+str(cb))




all = all+cb
cb = 0
for path in p13:
	times = 0;
	if "2" in path : 
		times =times+1
		
cb = cb+ times / len(p13)

for path in p14:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb+ times / len(p14)
for path in p15:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb+ times / len(p15)

for path in p21:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p21)
for path in p23:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p23)


for path in p24:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p24)
for path in p25:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p25)

for path in p31:
	times = 0;
	if "2" in path : 
		times =times+1
				
cb = cb + times / len(p31)
for path in p34:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p34)
for path in p35:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p35)
for path in p41:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p41)
for path in p43:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p43)
for path in p45:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p45)
for path in p51:
	times = 0;
	if "2" in path : 
		times =times+1
cb = cb + times / len(p51)
for path in p53:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p53)
for path in p54:
	times = 0;
	if "2" in path : 
		times =times+1

cb = cb + times / len(p54)

print("2----------------> " +str(cb) )

all = all+cb
cb = 0
for path in p12:
	times = 0;
	if "3" in path : 
		times =times+1
		
cb = cb+ times / len(p12)

for path in p14:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb+ times / len(p14)
for path in p15:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb+ times / len(p15)

for path in p21:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p21)


for path in p24:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p24)
for path in p25:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p25)

for path in p31:
	times = 0;
	if "3" in path : 
		times =times+1
				
cb = cb + times / len(p31)
for path in p32:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p32)
for path in p34:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p34)
for path in p35:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p35)
for path in p41:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p41)
for path in p42:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p42)
for path in p45:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p45)
for path in p51:
	times = 0;
	if "3" in path : 
		times =times+1
cb = cb + times / len(p51)
for path in p52:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p52)
for path in p54:
	times = 0;
	if "3" in path : 
		times =times+1

cb = cb + times / len(p54)

print("3----------------> " +str(cb) )

all = all+cb

cb = 0
for path in p12:
	times = 0;
	if "4" in path : 
		times =times+1
		
cb = cb+ times / len(p12)

for path in p13:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb+ times / len(p13)
for path in p15:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb+ times / len(p15)

for path in p21:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p21)


for path in p23:
	times = 0;
	if "4" in path : 
		times =times+1

cb = cb + times / len(p23)
for path in p25:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p25)

for path in p31:
	times = 0;
	if "4" in path : 
		times =times+1
				
cb = cb + times / len(p31)
for path in p32:
	times = 0;
	if "4" in path : 
		times =times+1

cb = cb + times / len(p32)

for path in p35:
	times = 0;
	if "4" in path : 
		times =times+1

cb = cb + times / len(p35)
for path in p41:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p41)
for path in p42:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p42)
for path in p43:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p43)
for path in p45:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p45)
for path in p51:
	times = 0;
	if "4" in path : 
		times =times+1
cb = cb + times / len(p51)
for path in p52:
	times = 0;
	if "4" in path : 
		times =times+1

cb = cb + times / len(p52)
for path in p53:
	times = 0;
	if "4" in path : 
		times =times+1

cb = cb + times / len(p53)

print("4----------------> " +str(cb) )

all = all+cb


cb = 0
for path in p12:
	times = 0;
	if "5" in path : 
		times =times+1
		
cb = cb+ times / len(p12)

for path in p13:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb+ times / len(p13)
for path in p14:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb+ times / len(p14)

for path in p21:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p21)


for path in p23:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p23)
for path in p24:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p24)

for path in p31:
	times = 0;
	if "5" in path : 
		times =times+1
				
cb = cb + times / len(p31)
for path in p32:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p32)

for path in p34:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p34)
for path in p41:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p41)
for path in p42:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p42)
for path in p43:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p43)

for path in p51:
	times = 0;
	if "5" in path : 
		times =times+1
cb = cb + times / len(p51)
for path in p52:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p52)
for path in p53:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p53)
for path in p55:
	times = 0;
	if "5" in path : 
		times =times+1

cb = cb + times / len(p55)

print("5----------------> " +str(cb) )
all = all+cb
print("db -------> "+str(all))

########### Iw

iw = 0
distance = 0
for p in nx.all_shortest_paths(G, source="1", target="1"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="1", target="2"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="1", target="3"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="1", target="4"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="1", target="5"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
### 2
for p in nx.all_shortest_paths(G, source="2", target="1"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="2", target="2"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="2", target="3"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="2", target="4"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="2", target="5"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
### 3
for p in nx.all_shortest_paths(G, source="3", target="1"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="3", target="2"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="3", target="3"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="3", target="4"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="3", target="5"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
	
### 4
for p in nx.all_shortest_paths(G, source="4", target="1"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
	
for p in nx.all_shortest_paths(G, source="4", target="2"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break	
for p in nx.all_shortest_paths(G, source="4", target="3"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="4", target="4"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="4", target="5"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
### 5 
for p in nx.all_shortest_paths(G, source="5", target="1"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="5", target="2"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="5", target="3"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="5", target="4"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
for p in nx.all_shortest_paths(G, source="5", target="5"):
	el=0
	for x in p:
		el = el+1
	print(el)
	distance = distance+el-1
	break
iw = distance
print("iw" + str(iw))
nx.wiener_index(G)
sum = 0
for key, value in nx.closeness_centrality(G,wf_improved=False).items():
	print(key, '	: ', value)
	sum = sum +1/value
	print(sum)
print(sum)
for key, value in nx.betweenness_centrality_source(G).items():
	sum = sum +value
	print(key, '	: ', value)
print(sum)
