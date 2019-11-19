import networkx as nx
import matplotlib.pyplot as plt
import os

# init graph
G=nx.MultiGraph()

# adding just one node:
G.add_node("london", seats=.425) # single node with a value seats (seats being a form of weight)
G.add_node("Birmingham", seats=.057)
G.add_node("liverpool", seats=.051)
G.add_node("Glasgow", seats=.023)
G.add_node("Edinburgh", seats=.018)
G.add_node("Cardiff", seats=.018)
G.add_node("Newport", seats=.014)
G.add_node("Swansea", seats=.014)
G.add_node("Belfast", seats=.012)
G.add_node("Aberdeen", seats=.010)
G.add_node("Derry", seats=.004)
G.add_node("Lisburn", seats=.004)

G.add_node("Labour-Party")
G.add_node("Conservative-Party")
G.add_node("Liberal-Democrats")
G.add_node("Brexit-Party")

filename = os.path.abspath(os.path.join("data", "londonSentiment.csv"))
print(filename)

with open(filename, 'r') as fin:
    header = fin.readline().strip().split(',')
    print(header)

    entries = []
    for line in fin:
        parts = line.strip().split(',')
        row = dict()
        for i, h in enumerate(header):
            row[h] = parts[i]

        entries.append(row)

# entries.sort(key=lambda r: int(r['Sentiment']))   ***sort

# while running through data assign the edges based of City, Party, sentimental value
for (e) in entries:
    print("{0}, {1}, sentiment: {2}".format(e['City'], e['Party'], e['Sentiment']))
    city = e['City']
    party = e['Party']
    weight = float(e['Sentiment'])*(G.nodes[city]['seats'])
    G.add_edge(city, party, weight=weight)

# printing nodes
print("Print all Nodes")
print(G.nodes())
print("Print all edges")
print(G.edges())

labourWeight = 0
conservativeWeight = 0
liberalDemocratWeight = 0
brexitWeight = 0

totalLabourPos = 0
totalLabourNeg = 0
totalConsPos = 0
totalConsNeg = 0

for (c, p, w) in G.edges.data('weight'):
#    print('(%s, %s, %f' % (c, p, w)) # printing edges with their weight
    tempWeight = w
    if tempWeight < 0:
        tempWeight *= .3
    if p == "Labour-Party":
        if w > 0:
            totalLabourPos += 1
        elif w < 0:
            totalLabourNeg += 1
        labourWeight += tempWeight
    elif p == "Conservative-Party":
        if w > 0:
            totalConsPos += 1
        elif w < 0:
            totalConsNeg += 1
        conservativeWeight += tempWeight
    elif p == "Liberal-Democrats":
        liberalDemocratWeight += tempWeight
    elif p == "Brexit-Party":
        brexitWeight += tempWeight

print(labourWeight)
print(conservativeWeight)
print(liberalDemocratWeight)
print(brexitWeight)
print(totalLabourPos)
print(totalLabourNeg)
print(totalConsPos)
print(totalConsNeg)



# print(type(G.nodes()))
# print(type(G.edges()))

# print the network as a graph
nx.draw(G)
plt.savefig("simple_path.png")
plt.show()