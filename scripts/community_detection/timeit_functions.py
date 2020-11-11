"""""""""""""""""""""""""""""""""""""""""""""""
|    SMM638: Network Analytics - Group 7      |
|---------------------------------------------|
| This python script contains functions       |
| to compare execution time among algorithms  |
|                                             |
"""""""""""""""""""""""""""""""""""""""""""""""

import time
from tqdm.notebook import tqdm
import numpy as np
import networkx as nx
import itertools
from networkx.algorithms.community import girvan_newman, modularity
from networkx import edge_betweenness_centrality as betweenness
from networkx.algorithms.community import greedy_modularity_communities
import community as community_louvain
import infomap
import igraph as ig
import leidenalg

def gn_time(G):
    
    # define a function to compute weighted centrality betweenness
    def most_central_edge(G):
        centrality = betweenness(G, weight = 'weight')
        return max(centrality, key = centrality.get)
    
    # initiate a list to store execution time for each algo
    algo_time = []
    
    for i in tqdm(range(10)):
        
        # start
        start_time = time.time()
        
        # fit the model
        if nx.is_weighted(G):
            solutions = girvan_newman(G, most_valuable_edge = most_central_edge)
        else:
            solutions = girvan_newman(G)

        # assign the number of times partitioning
        k = len(G.edges)

        # register modularity scores
        modularity_scores = dict()

        # initiate a maximum modularity score
        max_score = 0

        # initiate count (stopping criterion)
        count = 0

        # iterate over solutions
        for community in itertools.islice(solutions, k):
            solution = list(sorted(c) for c in community)
            score = modularity(G, solution)
            # store modularity score
            modularity_scores[len(solution)] = score
            if score > max_score:
                # save the community structure with highest modularity score
                community_structure = list(solution)
                max_score = score
                count = 0
            else:
                count = count + 1
            if count == 5:
                break
        
        algo_time.append(time.time() - start_time)
            
    return np.mean(algo_time)        
    

def cnm_time(G):

    # initiate a list to store execution time for each algo
    algo_time = []
    
    for i in tqdm(range(10)):
        
        # start
        start_time = time.time()
        
        # fit the model
        if nx.is_weighted(G):
            c = greedy_modularity_communities(G, weight = 'weight')
        else:
            c = greedy_modularity_communities(G)
        
        algo_time.append(time.time() - start_time)

    return np.mean(algo_time)  


def lv_time(G):

    # initiate a list to store execution time for each algo
    algo_time = []
    
    for i in tqdm(range(10)):
        
        # start
        start_time = time.time()
        
        # fit the model
        if nx.is_weighted(G):
            communities = community_louvain.best_partition(G, weight = 'weight')
        else:
            communities = community_louvain.best_partition(G)
        
        algo_time.append(time.time() - start_time)

    return np.mean(algo_time)         


def im_time(G):

    # initiate an infomap object
    im = infomap.Infomap()
    
    # add nodes
    im.add_nodes(G.nodes)
    
    # add edges and weights
    # transpose a numpy array to get arrays of first and second elements in edges
    sources = np.array(G.edges).T[0]
    targets = np.array(G.edges).T[1]
    weights = nx.get_edge_attributes(G, 'weight').values()
    if nx.is_weighted(G) == True:
        edges = zip(sources, targets, weights)
    elif nx.is_weighted(G) == False:
        edges = zip(sources, targets)
    im.add_links(edges)
    
    # initiate a list to store execution time for each algo
    algo_time = []
    
    for i in tqdm(range(10)):
    
        # start
        start_time = time.time()
        
        # run the model
        im.run()
        
        algo_time.append(time.time() - start_time)
     
    return np.mean(algo_time)


def ld_time(G):
    
    # initiate an igraph object
    g = ig.Graph()
    
    # add vertices
    g.add_vertices(G.nodes)
    
    # add edges
    g.add_edges(G.edges)
    
    # add weights
    if nx.is_weighted(G): 
        g.es['weight'] = list(nx.get_edge_attributes(G, 'weight').values())
       
    # initiate a list to store execution time for each algo
    algo_time = []
    
    for i in tqdm(range(10)):
    
        # start
        start_time = time.time()
        
        # fit the model
        partition = leidenalg.find_partition(g, leidenalg.ModularityVertexPartition)
        
        algo_time.append(time.time() - start_time)
     
    return np.mean(algo_time)

    