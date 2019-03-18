"""# -*- coding: utf-8 -*-

Created on Fri Feb 15 17:30:45 2019

@author: s159151
"""
import numpy
import random
import networkx as nx
import itertools
import collections
from networkx.algorithms import bipartite
from networkx.utils import py_random_state
from collections import Iterable



noPeople = 100000 #Variable that stores the number of people
noComs = noPeople//2 #Variable that stores the number of communities in this case always half of noPeople


ldeg_list = [1]*(noPeople//2) + [3]*(noPeople//2)
rdeg_list = [3]*(noComs//2) + [5]*(noComs//2)

#Consider file input

#Creating a list of half edges

lhalfedge_list = [[i+1]*ldeg_list[i] for i in range(noPeople)]
rhalfedge_list = [enumerate([j+1]*rdeg_list[j]) for j in range(noComs)]
lhalfedge_list = list(itertools.chain(*lhalfedge_list))
rhalfedge_list = list(itertools.chain(*rhalfedge_list))
#print(lhalfedge_list)
#print(rhalfedge_list)

#Matching the half edges

random.shuffle(rhalfedge_list)
#print(rhalfedge_list)
edge_list = list(zip(lhalfedge_list , rhalfedge_list))
#print(edge_list)

#Projects the matches to the projected graph. We assume a complete community structure

#prodG_list = []
#for k in range(len(edge_list)):
#    for m in range(len(edge_list)):
#        if edge_list[k][1][1] == edge_list[m][1][1] and k < m :
#            prodG_list.append((edge_list[k][0],edge_list[m][0]))
          
#print(prodG_list)

#G = nx.MultiGraph()
#G.add_edges_from(prodG_list)
#nx.draw(G)


#Now we have different community structures called cherry and house

cherry_list = [[(0,1), (1,2)]]*(noComs//2)
house_list = [[(0,1),(0,2),(0,4),(1,3),(1,4),(2,3)]]*(noComs//2)


#C = nx.MultiGraph()
#C.add_edges_from(cherry_list)
#nx.draw(C)

#H = nx.MultiGraph()
#H.add_edges_from(house_list)
#nx.draw(H)




graph_list = cherry_list + house_list
#print(graph_list)

#G = nx.MultiGraph()
#G.add_edges_from(graph_list)
#nx.draw(G)

#Projects the matches to the projected graph given a specific community structure

restrictedProdG_list = []
for n in range(len(edge_list)):
    for p in range(len(edge_list)):
        if edge_list[n][1][1] == edge_list[p][1][1] and n < p :
            if (edge_list[n][1][0], edge_list[p][1][0]) in graph_list[edge_list[n][1][1]-1]:
                restrictedProdG_list.append((edge_list[n][0],edge_list[p][0]))
            
#print(restrictedProdG_list)

#G = nx.MultiGraph()
#G.add_edges_from(restrictedProdG_list)
#nx.draw(G)


#Defines the function flatten which simply returns all numbers in a given list as seperate entries

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
            
#Returns a sorted list of people
            
flattenedProdG_list = list(flatten(restrictedProdG_list))
flattenedProdG_list.sort()
#print(flattenedProdG_list)

#Returns the degree of all people by counting how many times they occur in the above list

counter = collections.Counter(flattenedProdG_list)
counter_list = list(counter.values())
#print(counter_list)

#Returns the number of people with a certain degree

counter2 = collections.Counter(counter_list)
counter2_list = list(counter2.values())

#Calculates the degree distribution (should tend to the theoretical values as noPeople tends to infinity)

pk = []
for i in counter2_list:
    pk.append(i/len(counter_list))
print(pk)
print(sum(pk))