import networkx as nx 

# Read data from file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file]
    return data

# Function to build k-truss
def build_k_truss(G, k):
    H = G.copy()
    
    while True:
        edge_support = {e: 0 for e in H.edges()}
        for u, v in H.edges():
            common_neighbors = list(set(H[u]) & set(H[v]))
            for w in common_neighbors:
                if (u, w) in H.edges() and (v, w) in H.edges():
                    edge_support[(u, v)] += 1
        
        to_remove = [e for e in edge_support if edge_support[e] < k - 2]
        if not to_remove:
            break
        
        H.remove_edges_from(to_remove)
    
    return H

# Usage
filename = './dataset.txt'
data = read_data_from_file(filename)

# Create the graph
G = nx.Graph()
G.add_edges_from(data)

# Set the desired k value
k = 4

# Build k-truss
k_truss_graph = build_k_truss(G, k)

# Save k-truss graph to a file
nx.write_gexf(k_truss_graph, "k_truss_graph.gexf")
