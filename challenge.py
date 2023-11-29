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

# Function to print edges of the k-truss graph
def print_k_truss_edges(k_truss_graph):
    for u, v in k_truss_graph.edges():
        print(f"{u}  {v}")

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

print_k_truss_edges(k_truss_graph)
# Count triangles in the graph G
triangle_count = sum(nx.triangles(G).values()) // 3  # Dividing by 3 to account for each triangle being counted 3 times
print("Number of triangles in the graph:", triangle_count)
