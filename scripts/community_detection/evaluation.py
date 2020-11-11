"""""""""""""""""""""""""""""""""""""""""""""""
|    SMM638: Network Analytics - Group 7      |
|---------------------------------------------|
| This python script contains functions       |
| to evalue communities detection algorithms  |
|                                             |
"""""""""""""""""""""""""""""""""""""""""""""""

from collections import defaultdict
import pandas as pd
import networkx as nx
import networkx.algorithms.community as nx_comm
from community_detection.timeit_functions import *


def evaluate_execution_time(G, commu_list):
    
    # initiate a dictionary to store execution_time
    execution_time = {}
    
    # get the list of algo
    algo_list = []
    for c in commu_list:
        algo_list.append(c['algo'])
    
    # loop over each algo 100 times each and get the average
    for algo in tqdm(algo_list):
        if algo == 'Girvan-Newman':
            execution_time[algo] = gn_time(G)
        elif algo == 'Clauset-Newman-Moore':
            execution_time[algo] = cnm_time(G)
        elif algo == 'Louvain':
            execution_time[algo] = lv_time(G)
        elif algo == 'Infomap':
            execution_time[algo] = im_time(G)
        elif algo == 'Leiden':
            execution_time[algo] = ld_time(G)

    return execution_time
    
    
def evaluate_modularity(G, commu_list):
    
    # initiate a dictionary to store modularity
    modularities = {}
    
    # loop over all community structure
    for c in commu_list:
        communities = c['communities']
        # prepare element for modularity calculation
        commu = []
        # loop over communities in an algorithm
        for i in sorted(pd.Series(communities.values()).unique()):
            store_list = []
            # loop over all nodes
            for node in G.nodes:
                if communities[node] == i:
                    store_list.append(node)
            commu.append(store_list)
        # calculate modularity
        modularity = nx_comm.modularity(G, commu)
        # store value in `modularities`
        modularities[c['algo']] = modularity
    
    return modularities


def evaluate_coverage(G, commu_list):
    
    # initiate a dictionary to store coverages
    coverages = {}
    
    # loop over all community structure
    for c in commu_list:
        communities = c['communities']
        # prepare element for coverage calculation
        commu = []
        # loop over communities in an algorithm
        for i in sorted(pd.Series(communities.values()).unique()):
            store_list = []
            # loop over all nodes
            for node in G.nodes:
                if communities[node] == i:
                    store_list.append(node)
            commu.append(store_list)
        # calculate coverage
        coverage = nx_comm.coverage(G, commu)
        # store value in `coverages`
        coverages[c['algo']] = coverage
    
    return coverages


def evaluate_performance(G, commu_list):
    
    # initiate a dictionary to store performances
    performances = {}
    
    # loop over all community structure
    for c in commu_list:
        communities = c['communities']
        # prepare element for performance calculation
        commu = []
        # loop over communities in an algorithm
        for i in sorted(pd.Series(communities.values()).unique()):
            store_list = []
            # loop over all nodes
            for node in G.nodes:
                if communities[node] == i:
                    store_list.append(node)
            commu.append(store_list)
        # calculate performance
        performance = nx_comm.performance(G, commu)
        # store value in `performances`
        performances[c['algo']] = performance
    
    return performances


def robustness_test(G, commu_list):
    
    # initiate a dictionary to store community structure
    commu_structure = {}

    # loop over all community structure
    for c in commu_list:
        communities = c['communities']
        # prepare element for modularity calculation
        commu = []
        # loop over communities in an algorithm
        for i in sorted(pd.Series(communities.values()).unique()):
            store_list = []
            # loop over all nodes
            for node in G.nodes:
                if communities[node] == i:
                    store_list.append(node)
            commu.append(store_list)
        # store structure in `commu_structure`
        commu_structure[c['algo']] = commu
        
    # `store` keeps all the community structure a node is in from all algorithms as a value
    store = defaultdict(list)
    for node in G.nodes():
        for algo in commu_structure.keys():
            for community in commu_structure[algo]:
                if node in community:
                    store[node].append(community)
                    
    # generate the summary table which uses (Union - Intersection) as a metric: The closer to zero demonstrates
    # more robust segmentation. 
    result = {}
    for node in store:
        union_set = set()
        inter_set = set()
        for index, commu in enumerate(store[node]):
            if bool(union_set) == False:
                union_set = set(commu)
            else:
                union_set = union_set.union(set(commu))
            if bool(inter_set) == False:
                inter_set = set(commu)
            else:
                inter_set = inter_set.intersection(set(commu))
        result[node] = [len(union_set - inter_set), list(inter_set), list(union_set - inter_set)]
    
    summary = sorted(result.values())
    df = pd.DataFrame(summary)
    df = df.loc[df.astype(str).drop_duplicates().index].rename(columns = {0: 'metric',
                                                                          1: 'community ( I )',
                                                                          2: 'unmatched ( U - I )'})
    
    return df

        
        

    
    