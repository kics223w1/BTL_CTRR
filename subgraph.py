import networkx as nx
import matplotlib.pyplot as plt

# Function to read data from a file and add a column
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file]
    return data

# Function to add a column with a constant value
def add_column(data, constant_value):
    return [(x[0], x[1], constant_value) for x in data]

# Function to write data to a new file
def write_data_to_file(data, new_filename):
    with open(new_filename, 'w') as file:
        for line in data:
            file.write(' '.join(map(str, line)) + '\n')

filename = './dataset.txt'
data = read_data_from_file(filename)
constant_value = 1
data_with_column = add_column(data, constant_value)

new_filename = './updated_dataset.txt'
write_data_to_file(data_with_column, new_filename)
new_data = read_data_from_file(new_filename)

G = nx.DiGraph()  # Directed graph

for edges in new_data:
    G.add_edge(edges[0], edges[1], weight=edges[2])
    
shortest_paths = nx.single_source_dijkstra(G, source=0)

# Extract nodes reachable from node 0
reachable_nodes = shortest_paths[0]

# Create a subgraph with nodes reachable from node 0
subgraph_nodes = list(reachable_nodes.keys())  # Nodes reachable from node 0
subgraph = G.subgraph(subgraph_nodes)
for edge in subgraph.edges():
    print(edge)