import networkx as nx 

# Read data from file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file]
    return data
def counting_triangles(G):
    count = 0
    for node in G.nodes():
        neighbors = set(G.neighbors(node))
        for neighbor in neighbors:
            i = set(G.neighbors(neighbor)) & neighbors
            for j in i:
                if node < neighbor < j:
                    count += 1
    return count

# Usage
filename = './dataset.txt'
data = read_data_from_file(filename)

# Create the graph
G = nx.Graph()
G.add_edges_from(data)

count_triangles = counting_triangles(G)
print(count_triangles)
