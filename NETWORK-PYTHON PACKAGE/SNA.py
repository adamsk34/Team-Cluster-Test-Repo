import networkx as nx
import matplotlib.pyplot as plt
import os

# init graph
G=nx.MultiGraph()

# adding just one node:
G.add_node("london", seats=.425) # single node with a value seats (seats being a form of weight)
G.add_node("birmingham", seats=.057)
G.add_node("liverpool", seats=.051)
G.add_node("glasgow", seats=.023)
G.add_node("edinburgh", seats=.018)
G.add_node("cardiff", seats=.018)
G.add_node("newport", seats=.014)
G.add_node("swansea", seats=.014)
G.add_node("belfast", seats=.012)
G.add_node("aberdeen", seats=.010)
G.add_node("derry", seats=.004)
G.add_node("lisburn", seats=.004)

G.add_node("Labour-Party")
G.add_node("Conservative-Party")
G.add_node("Liberal-Democrats")
G.add_node("Brexit-Party")

dircName = "Calculated data"

london = 0
liverpool = 0
birmingham = 0
glasgowor = 0
edinburgh = 0
cardiff=0
newport=0
swansea=0
belfast=0
aberdeen=0
derry=0
lisburn=0

for subdir, dirs, files in os.walk(dircName):
    for file in files:
        filename = os.path.abspath(os.path.join(subdir, file))
        with open(filename, 'r') as fin:
            header = fin.readline().strip().split(',')
            entries = []
            for line in fin:
                parts = line.strip().split(',')
                row = dict()
                for i, h in enumerate(header):
                    row[h] = parts[i]

                entries.append(row)
        # while running through data assign the edges based of City, Party, sentimental value
        for (e) in entries:
            # print("{0}, {1}, {2} sentiment: {3}".format(e['City'], e['Party'], e['Leader'], e['Sentiment']))
            city = e['City']
            party = e['Party']
            leader = e['Leader']

            #pure sentemental
            #weight = float(e['Sentiment Value'])

            #sentemntal with city weights
            weight = float(e['Sentiment Value'])*(G.nodes[city]['seats'])

            #only add constant values of what city is worth based on if it is positive or negative
            #if float(e['Sentiment Value']) > 0:
             #   weight = (G.nodes[city]['seats'])
            #elif float(e['Sentiment Value']) < 0:
             #   weight = -(G.nodes[city]['seats'])

            G.add_edge(city, party, weight=weight)
            if(party == ""):
                G.add_edge(city, leader, weight=weight)

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
totalLiberalPos = 0
totalLiberalNeg = 0
totalBrexitPos = 0
totalBrexitNeg = 0



for (c, p, w) in G.edges.data('weight'):
    tempWeight = w

    #here we modify if the wight is negative we can change it
    if tempWeight < 0:
        tempWeight  = tempWeight
    if p == "Labour-Party" or p == "Jeremy-Corbyn":
        labourWeight += tempWeight
        if w > 0:
            totalLabourPos += 1
        elif w < 0:
            totalLabourNeg += 1
    elif p == "Conservative-Party" or p == "Borris-Johnson":
        conservativeWeight += tempWeight
        if w > 0:
            totalConsPos += 1
        elif w < 0:
            totalConsNeg += 1
    elif p == "Liberal-Democrats" or p == "jo-Swinson":
        liberalDemocratWeight += tempWeight
        if w > 0:
            totalLiberalPos += 1
        elif w < 0:
            totalLiberalNeg += 1
    elif p == "Brexit-Party" or p == "Nigel-Farage":
        brexitWeight += tempWeight
        if w > 0:
            totalBrexitPos += 1
        elif w < 0:
            totalBrexitNeg += 1


print("conservativeWeight: " , conservativeWeight , "pos: " , totalConsPos , "neg: " , totalConsNeg)
print("labourWeight " , labourWeight , "pos: " , totalLabourPos , "neg: " , totalLabourNeg)
print("liberalDemocratWeight " , liberalDemocratWeight, "pos: " ,totalLiberalPos , "neg: " ,totalLiberalNeg)
print("brexitWeight " ,  brexitWeight , "pos: " , totalBrexitPos , "neg: " , totalBrexitNeg)

print("londons total tweets: ", london)
print("liverpool total tweets: ", liverpool)




# print(type(G.nodes()))
# print(type(G.edges()))

# print the network as a graph
#nx.draw(G, with_labels=True, node_color='skyblue', node_size=250, edge_color='black', pos=nx.planar_layout(G))
#plt.savefig("simple_path.png")
#plt.show()