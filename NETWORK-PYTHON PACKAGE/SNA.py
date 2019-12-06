import networkx as nx
import os


ALPHA = 0.8

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


totalLabourWeightTF = 0
totalConservativeWeightTF = 0
totalLiberalDemocratWeightTF = 0
totalBrexitWeight = 0

totalLabourWeight = 0
totalConservativeWeight = 0
totalLiberalDemocratWeight = 0

totalLabourPos = 0
totalLabourNeg = 0
totalConsPos = 0
totalConsNeg = 0
totalLiberalPos = 0
totalLiberalNeg = 0
totalBrexitPos = 0
totalBrexitNeg = 0

for subdir, dirs, files in os.walk(dircName):
    labourWeight = 0
    conservativeWeight = 0
    liberalDemocratWeight = 0
    brexitWeight = 0

    totalConservativeWeightTF *= ALPHA
    totalLabourWeightTF *= ALPHA
    totalLiberalDemocratWeightTF *= ALPHA
    
    #make a new graph for each batch
    G = nx.MultiGraph()
    G.add_node("london", seats=.625)  # single node with a value seats (seats being a form of weight)
    G.add_node("birmingham", seats=.57)
    G.add_node("liverpool", seats=.51)
    G.add_node("glasgow", seats=.23)
    G.add_node("edinburgh", seats=.18)
    G.add_node("cardiff", seats=.18)
    G.add_node("newport", seats=.14)
    G.add_node("swansea", seats=.14)
    G.add_node("belfast", seats=.12)
    G.add_node("aberdeen", seats=.10)
    G.add_node("derry", seats=.04)
    G.add_node("lisburn", seats=.04)

    G.add_node("Labour-Party")
    G.add_node("Conservative-Party")
    G.add_node("Liberal-Democrats")
    G.add_node("Brexit-Party")

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


            G.add_edge(city, party, weight=weight)
            if(party == ""):
                G.add_edge(city, leader, weight=weight)

    for (c, p, w) in G.edges.data('weight'):
        tempWeight = w
        # here we modify if the wight is negative we can change it
        if tempWeight < 0:
            tempWeight = tempWeight
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
    totalConservativeWeightTF += conservativeWeight
    totalLabourWeightTF += labourWeight
    totalLiberalDemocratWeightTF += liberalDemocratWeight

    totalConservativeWeight += conservativeWeight
    totalLabourWeight += labourWeight
    totalLiberalDemocratWeight += liberalDemocratWeight



print("conservativeWeight: ", totalConservativeWeight, "pos: ", totalConsPos, "neg: ", totalConsNeg)
print("labourWeight ", totalLabourWeight, "pos: ", totalLabourPos, "neg: ", totalLabourNeg)
print("liberalDemocratWeight ", totalLiberalDemocratWeight, "pos: ", totalLiberalPos, "neg: ", totalLiberalNeg)
# print("brexitWeight " ,  brexitWeight , "pos: " , totalBrexitPos , "neg: " , totalBrexitNeg)

print("conservativeWeight with time fading: ", totalConservativeWeightTF, "pos: ", totalConsPos, "neg: ", totalConsNeg)
print("labourWeight with time fading ", totalLabourWeightTF, "pos: ", totalLabourPos, "neg: ", totalLabourNeg)
print("liberalDemocratWeight with time fading ", totalLiberalDemocratWeightTF, "pos: ", totalLiberalPos, "neg: ", totalLiberalNeg)


# printing nodes
#print("Print all Nodes")
#print(G.nodes())
#print("Print all edges")
#print(G.edges())







# print(type(G.nodes()))
# print(type(G.edges()))

# print the network as a graph
#nx.draw(G, with_labels=True, node_color='skyblue', node_size=250, edge_color='black', pos=nx.planar_layout(G))
#plt.savefig("simple_path.png")
#plt.show()