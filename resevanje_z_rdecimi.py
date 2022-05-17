import xml.etree.ElementTree as ET
import numpy as np
import funkcije as fn
from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import networkx as nx

tree = ET.parse('arnes-backbone-map_sl.xml')
root = tree.getroot()

points= dict()
labels = dict()
povezave =[]
for i,element in enumerate(root):
    #print(element.tag,element.attrib)
    if element.tag =='marker':
        podatki = element.attrib
        id = podatki['id']
        label = podatki['label']
        points[id]=i
        labels[i]=label

max_vozlisca = max(labels.keys())+1
matrika_sosednosti = np.zeros((max_vozlisca, max_vozlisca)).astype(int)
pretoki = np.zeros((max_vozlisca,max_vozlisca)).astype(int)

barve = {"#485E88":10, "#B325B8":20,"#00AEEF":1,"#008FC4":2,"#DCC944":200,"#FF8000":100,"#994C00":40, "#007676":10 }
count = 0
vzporedne = []
kapacitete = []
st_povezav = 0
for line in root:
    if line.tag=="line":
        poin = []
        for point in line:
            if point.attrib['id']!='split':
                id = points[point.attrib['id']]
                poin.append(id)
        if len(poin)==2:
            id1 = poin[0]
            id2 = poin[1]

            matrika_sosednosti[id1][id2]=1
            matrika_sosednosti[id2][id2]=1
        else:
            count+=1
        barva = line.attrib['color']
        if line.attrib['color']!="#FF0000":
            id1 = poin[0]
            id2 = poin[1]
            pretoki[id1][id2]+=int(barve[line.attrib['color']])
            pretoki[id2][id1]+=int(barve[line.attrib['color']])
            vzporedne.append((id1, id2))
            kapacitete.append(int(barve[line.attrib['color']]))
            matrika_sosednosti[id1][id2]=1
            matrika_sosednosti[id2][id1]=1
            st_povezav+=1
        else:
            id1 = poin[0]
            id2 = poin[1]
            pretoki[id1][id2]+=10
            pretoki[id2][id1]+=10
            vzporedne.append((id1, id2))
            kapacitete.append(10)
            matrika_sosednosti[id1][id2]=1
            matrika_sosednosti[id2][id1]=1
            st_povezav+=1




(matrika_pretokov, pot, maks) = fn.najvecji_pretok(matrika_sosednosti,pretoki,95,4)
fn.narisi_grafa(matrika_pretokov,labels,pot)
print(maks)
print(maks.residual)

G = nx.Graph()

label2 = dict()
for i in range(len(pot)):
    for j in range(len(pot)):
        if pot[i][j]!=0:
            G.add_edge(i, j, weight=abs(pot[i][j]))
            label2[i]=labels[i]
            label2[j]=labels[j]


pos = nx.shell_layout(G,  scale=50, )  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=100)
# edges
labels_edge = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edges(G, pos )
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels_edge)

# labels
nx.draw_networkx_labels(G, pos,labels=label2, font_family="sans-serif")

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.show()


