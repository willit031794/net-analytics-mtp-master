"""""""""""""""""""""""""""""""""""""""""""""""
|    SMM638: Network Analytics - Group 7      |
|---------------------------------------------|
| This python script contains a function      |
| to plot 3d network graph                    |
|                                             |
"""""""""""""""""""""""""""""""""""""""""""""""


import os
import numpy as np
import networkx as nx
import plotly.offline as py
import plotly.graph_objs as go

def plot_3d(G, community_structure):
    
    # set seed for coordinate
    np.random.seed(7)
    
    # set-up
    algo = community_structure['algo']
    communities = community_structure['communities']
    
    # get nodes name and its corresponding community as well as degrees
    labels = []
    group = []
    degrees = []
    for node in G.nodes:
        if len(nx.get_node_attributes(G, 'name')) > 0:
            labels.append(nx.get_node_attributes(G, 'name')[node])
        else:
            labels.append(node)
        group.append(communities[node])
        degrees.append(G.degree[node])
    
    # get the node positions
    pos = nx.kamada_kawai_layout(G, weight = 'weight', dim = 3, scale = 2)
    
    # get data for the Plotly
    # node coordinates, edge coordinates
    Xn=[pos[k][0] for k in range(len(G.nodes))]
    Yn=[pos[k][1] for k in range(len(G.nodes))]
    Zn=[pos[k][2] for k in range(len(G.nodes))]
    Xe=[]
    Ye=[]
    Ze=[]
    for e in G.edges:
        # coordinate of sources, targets
        Xe.extend([pos[e[0]][0],pos[e[1]][0], None])
        Ye.extend([pos[e[0]][1],pos[e[1]][1], None])
        Ze.extend([pos[e[0]][2],pos[e[1]][2], None])
    
    # edges
    trace1=go.Scatter3d(x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        line=dict(color='rgb(125,125,125)',
                                  width=1),
                        hoverinfo='text'
                       )
    
    # nodes
    trace2=go.Scatter3d(x=Xn,
                        y=Yn,
                        z=Zn,
                        mode='markers',
                        name='characters',
                        marker=dict(symbol='circle',
                                    size=degrees,
                                    color=group,
                                    colorscale='Edge',
                                    line=dict(color='rgb(50,50,50)',
                                              width=1)
                                   ),
                        text=labels,
                        hovertemplate = "<b>Node: %{text}</b> <br>Degree: %{marker.size} <br>Community: %{marker.color}<extra></extra>",
                        hoverinfo='text'
                       )

    axis=dict(
        showbackground=False,
        showline=False,
        zeroline=False,
        showgrid=False,
        showticklabels=False,
        title=''
    )

    layout = go.Layout(
         title="{}: {} Network".format(algo, G.name),
         width=1000,
         height=800,
         showlegend=False,
         scene=dict(
             xaxis=dict(axis),
             yaxis=dict(axis),
             zaxis=dict(axis)),
        margin=dict(t=50),
        hovermode='closest'
    )
    
    data=[trace1, trace2]
    fig=go.Figure(data=data, layout=layout)
    
    #save plot as html
    path = os.path.join('output', 'viz_{}_{}.html'.format(G.name.lower(), algo.lower()))
    fig.write_html(path)
    py.iplot(fig, filename='{}'.format(G.name))
    print("The plot was saved to: `{}`".format(path))
    
    return None
    