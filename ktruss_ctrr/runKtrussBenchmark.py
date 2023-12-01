
from ktruss import ktruss
import os, sys, argparse
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Use the pandas package if available
#import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("input_filename", nargs="?", action="store", type=str, default=".../testcase_ktruss.txt")
args = parser.parse_args()

inc_mtx_file = args.input_filename

if not os.path.isfile(inc_mtx_file):
	print("File doesn't exist: '{}'!".format(inc_mtx_file))
	sys.exit(1)

E=ktruss(inc_mtx_file,3)
print(E)
G = nx.Graph()

# Thêm cạnh và đỉnh từ ma trận incidence
num_nodes, num_edges = E.shape
for i in range(num_nodes):
    G.add_node(i)

for j in range(num_edges):
    edge_indices = np.where(E[:, j] != 0)[0]
    if len(edge_indices) == 2:
        G.add_edge(edge_indices[0], edge_indices[1])

# Vẽ đồ thị
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=10, font_color='black', font_weight='bold', font_family='sans-serif')

# Hiển thị đồ thị
plt.show()
