import xml.etree.ElementTree as ET
import numpy as np
import funkcije as fn
from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import networkx as nx


graf = nx.Graph()
graf.add_edge(0,1)
graf.add_edge(1,2)
graf.add_edge(1,3)
graf.add_edge(1,4)
graf.add_edge(4,5)
graf.add_edge(4,6)
plt.figure()
pos = nx.spring_layout(graf,)
nx.draw(graf,pos, node_color='orange', node_size=70)
nx.draw_networkx_labels(graf, pos,)
labels = nx.get_edge_attributes(graf, "weight")
nx.draw_networkx_edge_labels(graf, pos, edge_labels=labels,)
plt.show()