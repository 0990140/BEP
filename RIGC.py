# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:30:45 2019

@author: s159151
"""
import numpy
import random
import networkx as nx
import itertools
from networkx.algorithms import bipartite
from networkx.utils import py_random_state


noPeople = 4 #Variable that stores the number of people
noComs = noPeople//2 #Variable that stores the number of communities in this case always half of noPeople


ldeg_list = [1]*(noPeople//2) + [3]*(noPeople//2)
rdeg_list = [3]*(noComs//2) + [5]*(noComs//2)

#Consider file input

#Creating a list of half edges

lhalfedge_list = [[i+1]*ldeg_list[i] for i in range(noPeople)]
rhalfedge_list = [[j+1]*rdeg_list[j] for j in range(noComs)]
lhalfedge_list = list(itertools.chain(*lhalfedge_list))
rhalfedge_list = list(itertools.chain(*rhalfedge_list))
print(lhalfedge_list)
print(rhalfedge_list)

#Matching the half edges

random.shuffle(rhalfedge_list)
print(rhalfedge_list)
edge_list = list(zip(lhalfedge_list , rhalfedge_list))
print(edge_list)

prodG_list = []
for k in range(len(edge_list)):
    for m in range(len(edge_list)):
        if edge_list[k][1] == edge_list[m][1] and k < m :
            prodG_list.append((edge_list[k][0],edge_list[m][0]))
          
print(prodG_list)



nx.draw(nx.complete_graph(3)) #Half of the given communities look like this
nx.draw(nx.complete_graph(5)) #Half of the given communities look like this

#Questions:
#Can I create an array of graphs somehow? Maybe handle as objects
#I need to implement the matching process somehow, maybe handle as objects