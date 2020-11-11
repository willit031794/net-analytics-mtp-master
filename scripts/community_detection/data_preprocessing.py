"""""""""""""""""""""""""""""""""""""""""""""""
|    SMM638: Network Analytics - Group 7      |
|---------------------------------------------|
| This python script contains a function      |
| to load and process Star-Wars network graph |
|                                             |
"""""""""""""""""""""""""""""""""""""""""""""""


import os
import json
import pandas as pd
import networkx as nx

def load_starwars_graph():
    # setup data path
    base_path = os.path.join('..', 'datasets')
    file_path = os.path.join(base_path, 'starwars-full-interactions.json')
    
    with open(file_path) as json_file:
        data = json.load(json_file)
    
    # set-up
    df_nodes = pd.DataFrame(data['nodes'])
    df_edges = pd.DataFrame(data['links'])
    
    df_nodes.reset_index(inplace = True)

    df_nodes.rename(columns = {'index' : 'node_id'}, inplace = True)
    
    nodes_list = list(df_nodes.node_id)
    weighted_edges_list = list(zip(df_edges.source, df_edges.target, df_edges.value))
    
    # initialize a new graph object
    G = nx.Graph()

    # define the graph's name
    G.name = "Star-Wars"

    # populate the graph with nodes
    G.add_nodes_from(nodes_list)
    # add name attribute
    nx.set_node_attributes(G, df_nodes.name, name = 'name')

    # populate the graph with edges
    G.add_weighted_edges_from(weighted_edges_list, weight = 'weight')

    # print graph info
    print(nx.info(G))
    
    return G
