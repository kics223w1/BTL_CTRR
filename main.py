import networkx as nx
import matplotlib.pyplot as plt

# Function to read data from a file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file]
    return data

filename = './dataset.txt'
data = read_data_from_file(filename)

# Create an undirected graph
G = nx.Graph()

# Add edges from the data
G.add_edges_from(data)


# Perform BFS traversal
start_node = 0  # Choose the starting node for BFS
bfs_result = list(nx.bfs_edges(G, source=start_node))

print("BFS Traversal:")
for edge in bfs_result:
    print(edge)
