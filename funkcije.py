from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import networkx as nx
def najvecji_pretok(matrika_sosednosti, matrika_kapacitet, izvor,ponor):
    matrika_prenosov = matrika_kapacitet*matrika_sosednosti
    matrika_prenosov_csr = csr_matrix(matrika_kapacitet*matrika_sosednosti)
    maksimalni_pretok = maximum_flow(matrika_prenosov_csr,izvor,ponor)
    pot = maksimalni_pretok.residual.toarray()*(-1)
    return (matrika_prenosov,pot, maksimalni_pretok)

def narisi_grafa(matrika_prenosov, label,pot):
    G = nx.from_numpy_matrix(matrika_prenosov)
    plt.figure()
    pos = nx.random_layout(G,)
    nx.draw(G,pos, node_color='orange')
    nx.draw_networkx_labels(G, pos,labels=label)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    pot_pretoka = nx.from_numpy_matrix(pot)
    plt.figure()
    nx.draw(pot_pretoka, pos, node_color='hotpink', )
    nodes = sorted(nx.path_graph(G))
    nx.draw_networkx_labels(G, pos, labels=label)
    labels = nx.get_edge_attributes(pot_pretoka, "weight")
    nx.draw_networkx_edge_labels(pot_pretoka, pos, edge_labels=labels)
    plt.show()
