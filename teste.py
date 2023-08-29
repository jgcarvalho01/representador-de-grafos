import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

print(G.nodes()) 
print(G.edges) 

# Desenha o grafo
nx.draw(G, with_labels=True)
plt.show()  # Mostra a visualização do grafo