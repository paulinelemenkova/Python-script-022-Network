#!/usr/bin/env python
# coding: utf-8

# In[31]:


# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
# Build a dataframe with your connections
df = pd.DataFrame({ 'from':['Statistical Analysis', 'Visualization', 'Modelling','Statistical Analysis',   ], 
'to':['Geospatial \nData', 'Statistical Analysis', 'Plotting', 'Modelling', ]})
df
 
# Build your graph
G = nx.DiGraph()   # or DiGraph, 
G = nx.from_pandas_edgelist(df, 'from', 'to')
pos = nx.spring_layout(G)

    
# Graph with Custom nodes:
nx.draw(G, with_labels=True, node_size=2000, node_color="#ffd900", node_shape="s", alpha=0.5, linewidths=30)

plt.title("Workflow Network of Geospatial Analysis")
plt.show()

