#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# build a dataframe with connections
df = pd.DataFrame({'from':['Statistical Analysis', 'Visualization',
                           'Modelling','Statistical Analysis'],
                  'to':['Geospatial \nData', 'Statistical Analysis',
                        'Plotting', 'Modelling']
                  }
                  )
df

# build a graph
G = nx.DiGraph()   # or DiGraph,
G = nx.from_pandas_edgelist(df, 'from', 'to')
pos = nx.spring_layout(G)

# plotting graph with custom nodes:
nx.draw(G, with_labels=True, node_size=2000,
        node_color="#ee827c", node_shape="s",
        alpha=0.5, linewidths=30
        )

plt.title("Workflow Network of Geospatial Analysis")

# visualize
plt.subplots_adjust(top=0.85, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35
                    )
plt.savefig('plot_Netw.png', dpi=300)
plt.show()
