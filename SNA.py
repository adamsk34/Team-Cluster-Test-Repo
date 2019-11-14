import networkx as nx
import matplotlib.pyplot as plt

# init graph
G=nx.Graph()

# adding just one node:
G.add_node("England", seats=100) # single node with a value seats (seats being a form of weight)
# adding a list of nodes:
G.add_nodes_from(["Scotland", "Whales", "Ireland"]) #multiple nodes
# modifying nodes
G.nodes["England"]['seats'] = 200 # change amount of seats for england
G.nodes["Scotland"]['seats'] = 300 # set amount of seats for Scotland

if G.nodes["England"]['seats'] > G.nodes["Scotland"]['seats']:
    print("England has more seats")
else:
    print("Scotland has more seats")

# adding a single edge
G.add_edge("Scotland", "Whales", weight=1)
edge = ("Scotland", "Ireland")
G.add_edge(*edge)

# adding list of edges
G.add_edges_from([("England", "Scotland"),("England", "Whales"), ("England", "Ireland")])

# printing edges
print("Print all Nodes")
print(G.nodes())
print("Print all edges")
print(G.edges())
print(type(G.nodes()))
print(type(G.edges()))

# print the network as a graph
nx.draw(G)
plt.savefig("simple_path.png")
plt.show()