import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd

# If you want to separate some part of code
# %%
# Get nodes from .txt
G = nx.read_edgelist(f'CA-AstroPh-Not-Directed.txt')

# Print info about it
print(nx.info(G))

# Print number of nodes and edges separately
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))

# Print whether graph is directed or not
print(nx.is_directed(G))

# Choose random nodes
chosen_nodes = random.sample(G.nodes, 18000)

# Get subgraph from full and randomly selected part of it
H = nx.subgraph(G, chosen_nodes)

# Print info about subgraph
print(nx.info(H))

nx.draw(H, node_size=25)
plt.show()

# %%
# Sort data by time
data = pd.read_csv('email-Eu-core-temporal.txt',
                   sep=" ",
                   header=None,
                   names=["Nodes", "Edges", "Temp"])

data_sorted = data.sort_values(['Temp'])

print(data_sorted)

data_two_columns = data_sorted.drop(columns="Temp")

print(data_two_columns)

# %%
# Separated data to 4 snapshots

first_snapshot = data_two_columns.head(200)
second_snapshot = data_two_columns.iloc[200:400]
third_snapshot = data_two_columns.iloc[400:600]
fourth_snapshot = data_two_columns.iloc[600:800]

print(first_snapshot)
print(second_snapshot)
print(third_snapshot)
print(fourth_snapshot)

# %% Save snapshots separated by time to the files
first_snapshot.to_csv('first_snapshot.txt',
                      encoding='utf-8',
                      index=False,
                      sep=" ",
                      header=None)

print("first_snapshot file successfully save")

second_snapshot.to_csv('second_snapshot.txt',
                       encoding='utf-8',
                       index=False,
                       sep=" ",
                       header=None)

print("second_snapshot file successfully save")

third_snapshot.to_csv('third_snapshot.txt',
                      encoding='utf-8',
                      index=False,
                      sep=" ",
                      header=None)

print("third_snapshot file successfully save")

fourth_snapshot.to_csv('fourth_snapshot.txt',
                       encoding='utf-8',
                       index=False,
                       sep=" ",
                       header=None)

print("fourth_snapshot file successfully save")

# %% Plot the snapshots

G = nx.read_edgelist("first_snapshot.txt")

print(nx.info(G))

nx.draw(G, node_size=25)
plt.show()

G = nx.read_edgelist("second_snapshot.txt")

print(nx.info(G))

nx.draw(G, node_size=25)
plt.show()

G = nx.read_edgelist("third_snapshot.txt")

print(nx.info(G))

nx.draw(G, node_size=25)
plt.show()

G = nx.read_edgelist("fourth_snapshot.txt")

print(nx.info(G))

nx.draw(G, node_size=25)
plt.show()
